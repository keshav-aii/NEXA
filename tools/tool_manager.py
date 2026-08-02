from tools.app_tools import run as run_app


def choose_tool(command):

    command = command.lower()

    if command.startswith("open "):
        app = command.replace("open ", "")
        return run_app(app)

    return None