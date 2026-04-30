import wikipedia


def search_wikipedia(query: str):

    try:

        wikipedia.set_lang("en")

        summary = wikipedia.summary(query, sentences=2)

        return summary

    except wikipedia.exceptions.DisambiguationError as e:

        return f"There are multiple results for {query}. Please be more specific."

    except wikipedia.exceptions.PageError:

        return f"Sorry, I could not find anything about {query}."

    except Exception as e:

        print("WIKI ERROR:", e)

        return "Wikipedia search failed."