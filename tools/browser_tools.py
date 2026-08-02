import webbrowser


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube..."


def search_youtube(query):
    query = query.replace(" ", "+")

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )

    return f"Searching YouTube for {query.replace('+', ' ')}..."