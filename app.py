from dotenv import load_dotenv
from providers.google_gemini import chat as google_chat

def main():
    load_dotenv()

    print("Google Gemini Agent Starter (CLI)")
    print("Type 'exit' to quit, 'reset' to clear memory.\n")

    memory = []

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "exit":
            break
        if user_input.lower() == "reset":
            memory.clear()
            print("Conversation reset.\n")
            continue

        memory.append({"role": "user", "content": user_input})
        response = google_chat(memory)
        memory.append({"role": "assistant", "content": response})

        print(f"\nAssistant: {response}\n")

if __name__ == "__main__":
    main()
