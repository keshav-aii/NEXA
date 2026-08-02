from brain.brain import ask_nexa
from automation.automation import open_app

print("===================================")
print("        NEXA AI Assistant")
print("Type 'exit' to close.")
print("===================================")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    if user.lower().startswith("open "):

        app_name = user.lower().replace("open ", "")

        result = open_app(app_name)

        print("\nNEXA:", result)

        continue

    reply = ask_nexa(user)

    print("\nNEXA:", reply)