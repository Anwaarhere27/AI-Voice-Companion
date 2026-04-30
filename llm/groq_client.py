import os
from groq import Groq
from dotenv import load_dotenv
from memory.conversation_memory import conversation

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


SYSTEM_PROMPT = """
You are a friendly AI voice companion.

Keep responses:
- short
- natural
- conversational
- human-like

Avoid long paragraphs.
"""


def ask_groq(user_text):

    conversation.append({
        "role": "user",
        "content": user_text
    })

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + conversation

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )

    reply = completion.choices[0].message.content

    conversation.append({
        "role": "assistant",
        "content": reply
    })

    return reply