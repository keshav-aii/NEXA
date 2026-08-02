from brain.brain import ask_nexa
from tools.tool_manager import choose_tool
from voice.speaker import speak
from voice.listener import listen

print("===================================")
print("        NEXA AI Assistant")
print("Type 'exit' to close.")
print("===================================")

while True:

    user = listen()

    print(f"\nYou: {user}")

    if user.lower() == "exit":
        break

    result = choose_tool(user)

    if result:
        print("\nNEXA:", result)
        speak(result)
        continue
        

    reply = ask_nexa(user)

    print("\nNEXA:", reply)
    speak(reply)