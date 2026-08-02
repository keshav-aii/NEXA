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


def search_google(query):
    query = query.replace(" ", "+")
    webbrowser.open(
        f"https://www.google.com/search?q={query}"
    )
    return f"Searching Google for {query.replace('+', ' ')}..."


def open_github():
    webbrowser.open("https://github.com")
    return "Opening GitHub..."


def open_gmail():
    webbrowser.open("https://mail.google.com")
    return "Opening Gmail..."


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")
    return "Opening ChatGPT..."


def open_linkedin():
    webbrowser.open("https://www.linkedin.com")
    return "Opening LinkedIn..."