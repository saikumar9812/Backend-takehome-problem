import requests
import pandas as pd
import xml.etree.ElementTree as ET
import re
from typing import List, Dict, Any

class PubMedFetcher:
    SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def __init__(self, query: str):
        self.query = query

    def fetch_papers(self) -> str:
        search_params = {
            "db": "pubmed",
            "term": self.query,
            "retmode": "json",
            "retmax": 100
        }
        search_response = requests.get(self.SEARCH_URL, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()
        id_list = search_data["esearchresult"]["idlist"]

        fetch_params = {
            "db": "pubmed",
            "id": ",".join(id_list),
            "retmode": "xml"
        }
        fetch_response = requests.get(self.FETCH_URL, params=fetch_params)
        fetch_response.raise_for_status()
        return fetch_response.text

    def filter_non_academic_authors(self, xml_data: str) -> List[Dict[str, Any]]:
        root = ET.fromstring(xml_data)
        filtered_papers = []

        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

        for article in root.findall(".//PubmedArticle"):
            pub_date = article.find(".//PubDate")
            if pub_date is not None:
                year = pub_date.findtext("Year")
                month = pub_date.findtext("Month")
                day = pub_date.findtext("Day")
                publication_date = f"{year}-{month}-{day}" if year and month and day else year
            else:
                publication_date = None

            paper = {
                "PubmedID": article.findtext(".//PMID"),
                "Title": article.findtext(".//ArticleTitle"),
                "Publication Date": publication_date,
                "Non-academic Author(s)": [],
                "Company Affiliation(s)": [],
                "Corresponding Author Email": None
            }
            for author in article.findall(".//Author"):
                affiliation = author.findtext("AffiliationInfo/Affiliation")
                email = None
                if affiliation:
                    email_match = email_pattern.search(affiliation)
                    if email_match:
                        email = email_match.group(0)
                if affiliation and "university" not in affiliation.lower():
                    paper["Non-academic Author(s)"].append(author.findtext("LastName"))
                    paper["Company Affiliation(s)"].append(affiliation)
                if email and not paper["Corresponding Author Email"]:
                    paper["Corresponding Author Email"] = email
            if paper["Non-academic Author(s)"]:
                filtered_papers.append(paper)
        return filtered_papers

    def to_csv(self, papers: List[Dict[str, Any]], filename: str):
        df = pd.DataFrame(papers)
        df.to_csv(filename, index=False)