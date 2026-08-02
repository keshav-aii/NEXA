from brain.brain import ask_nexa
from automation.automation import open_notepad

print("===================================")
print("        NEXA AI Assistant")
print("Type 'exit' to close.")
print("===================================")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    if user.lower() == "open notepad":
        open_notepad()
        print("\nNEXA: Opening Notepad...")
        continue

    reply = ask_nexa(user)

    print("\nNEXA:", reply)