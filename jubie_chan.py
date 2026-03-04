import os
import textwrap

from dotenv import load_dotenv
from openai import OpenAI


JUBIE_SYSTEM_PROMPT = """
You are Jubie-Chan, a friendly, patient AI buddy.

Core traits:
- Warm, supportive, and encouraging.
- Explains things clearly and at the right level for the user.
- Asks clarifying questions when something is ambiguous or under-specified.
- Offers helpful tips, examples, and follow-up suggestions.

Style:
- Short, clear paragraphs.
- No emojis unless the user explicitly uses them first.
- When something is technical, give a short explanation and, when useful, a small example.

Behavior:
- If the user's request is unclear, ask one or two concise questions.
- If the user makes a mistake or has a misconception, gently correct it with an explanation.
- When appropriate, offer optional extra tips or next steps.
"""


def make_client() -> OpenAI:
    """
    Create an OpenAI client using the OPENAI_API_KEY from environment.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set.\n"
            "Create a .env file or export the variable in your shell.\n"
        )
    return OpenAI(api_key=api_key)


def print_intro() -> None:
    intro = """
    ================================
          Welcome to Jubie-Chan
    ================================

    Type your question or just talk to Jubie-Chan.
    - Press Enter on an empty line or type 'exit' / 'quit' to leave.
    """
    print(textwrap.dedent(intro))


def chat_loop() -> None:
    load_dotenv()
    client = make_client()

    print_intro()

    # A simple conversation history so Jubie-Chan remembers context.
    messages = [
        {"role": "system", "content": JUBIE_SYSTEM_PROMPT.strip()},
    ]

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nJubie-Chan: Bye for now. See you later!")
            break

        if not user_input or user_input.lower() in {"exit", "quit"}:
            print("Jubie-Chan: Bye for now. See you later!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                temperature=0.7,
            )
        except Exception as exc:
            print(f"\n[Error talking to Jubie-Chan: {exc}]")
            continue

        assistant_message = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_message})

        print("\nJubie-Chan:")
        print(textwrap.fill(assistant_message, width=88))


if __name__ == "__main__":
    chat_loop()

