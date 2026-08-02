from brain.brain import ask_nexa
from tools.tool_manager import choose_tool

print("===================================")
print("        NEXA AI Assistant")
print("Type 'exit' to close.")
print("===================================")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    result = choose_tool(user)

    if result:
        print("\nNEXA:", result)
        continue

    reply = ask_nexa(user)

    print("\nNEXA:", reply)