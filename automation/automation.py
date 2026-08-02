import subprocess
from automation.apps import APPS


def open_app(app_name):

    app_name = app_name.lower()

    if app_name in APPS:
        subprocess.Popen(APPS[app_name])
        return f"Opening {app_name}..."

    return f"Sorry, I couldn't find {app_name}."