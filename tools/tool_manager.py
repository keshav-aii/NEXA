from tools.app_tools import run as run_app
from tools.browser_tools import open_youtube

def choose_tool(command):

    command = command.lower()

    if command == "open youtube":
       
        return open_youtube()

    if command.startswith("open "):
        app = command.replace("open ", "")
        return run_app(app)

    return None