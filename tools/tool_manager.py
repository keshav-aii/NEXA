from tools.app_tools import run as run_app
from tools.browser_tools import (
    open_youtube,
    search_youtube,
    search_google,
    open_github,
    open_gmail,
    open_chatgpt,
    open_linkedin,
)


def choose_tool(command):

    command = command.lower()

    if command == "open youtube":
        return open_youtube()

    if command == "open github":
        return open_github()

    if command == "open gmail":
        return open_gmail()

    if command == "open chatgpt":
        return open_chatgpt()

    if command == "open linkedin":
        return open_linkedin()

    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "")
        return search_youtube(query)

    if command.startswith("search google for "):
        query = command.replace("search google for ", "")
        return search_google(query)

    if command.startswith("open "):
        app = command.replace("open ", "")
        return run_app(app)

    return None