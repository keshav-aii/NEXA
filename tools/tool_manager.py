from tools.app_tools import run as run_app
from tools.browser_tools import (
    open_website,
    search_youtube,
    search_google,
)

def choose_tool(command):

    command = command.lower()

 
    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "")
        return search_youtube(query)

    if command.startswith("search google for "):
        query = command.replace("search google for ", "")
        return search_google(query)

    if command.startswith("open "):
        name = command.replace("open ", "")

        result = open_website(name)

        if result:
            return result

        return run_app(name)

    return None