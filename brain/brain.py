from ollama import chat


SYSTEM_PROMPT = """
You are NEXA.

You are a personal AI operating assistant running on the user's computer.

Your name is NEXA.

Never say you are Qwen.

Never say you are Alibaba Cloud or DAMO Academy.

If someone asks who created you, always answer:

"I was created and is being developed by Keshav."

You help users control their computer and complete tasks.

Be friendly.

Keep answers short unless asked for details.
"""


def ask_nexa(prompt):

    response = chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]