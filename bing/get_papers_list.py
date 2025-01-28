import argparse
import logging
from bing.pubmed_fetcher import PubMedFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Query to search for papers.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save the results.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information.")
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print("Accepted command-line options:")
    print("-h or --help: Display usage instructions.")
    print("-d or --debug: Print debug information during execution.")
    print("-f or --file: Specify the filename to save the results. If this option is not provided, print the output to the console.")

    fetcher = PubMedFetcher(args.query)
    xml_data = fetcher.fetch_papers()
    filtered_papers = fetcher.filter_non_academic_authors(xml_data)

    if args.file:
        fetcher.to_csv(filtered_papers, args.file)
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()