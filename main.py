from brain.brain import ask_nexa

print("===================================")
print("        NEXA AI Assistant")
print("Type 'exit' to close.")
print("===================================")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    reply = ask_nexa(user)

    print("\nNEXA:", reply)