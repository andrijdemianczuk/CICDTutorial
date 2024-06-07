import wikipedia


def summarize_wikipedia(query="War Goddess", length=1):
    try:
        result = wikipedia.summary(query, length)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return e.options
    except wikipedia.exceptions.PageError:
        return "No results found."


def search_wikipedia(query):
    try:
        result = wikipedia.search(query)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return e.options
    except wikipedia.exceptions.PageError:
        return "No results found."
