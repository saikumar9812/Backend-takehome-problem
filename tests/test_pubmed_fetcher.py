import pytest
from bing.pubmed_fetcher import PubMedFetcher

def test_fetch_papers():
    fetcher = PubMedFetcher("cancer")
    result = fetcher.fetch_papers()
    assert result is not None
    assert "<PubmedArticle>" in result