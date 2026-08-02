from tools.app_tools import run as run_app
from tools.browser_tools import open_youtube, search_youtube


def choose_tool(command):

    command = command.lower()

    if command == "open youtube":
        return open_youtube()

    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "")
        return search_youtube(query)

    if command.startswith("open "):
        app = command.replace("open ", "")
        return run_app(app)

    return None