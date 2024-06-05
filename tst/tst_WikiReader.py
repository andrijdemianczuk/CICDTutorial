from src.WikiReader import search_wikipedia
def test_search_wikipedia():
    result = search_wikipedia (query="Goldendoodle", length=10)
    assert "goldendoodle" in result