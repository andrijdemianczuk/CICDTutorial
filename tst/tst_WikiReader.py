from src.WikiReader import summarize_wikipedia


def test_search_wikipedia():
    result = summarize_wikipedia(query="Goldendoodle", length=10)
    assert "goldendoodle" in result
