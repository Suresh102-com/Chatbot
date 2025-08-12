# Start the chatbot function
def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot.")
    print("Type 'bye', 'exit', or 'quit' anytime to end the chat.\n")

    while True:
        # Get the user's message
        user_input = input("You: ").strip().lower()

        # Check for exit keywords
        if user_input in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day! 👋")
            break

        # Now check for certain keywords or phrases
        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great, thanks for asking! How about you?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm ChatBot 1.0 — your virtual friend.")
        
        elif "weather" in user_input:
            print("🤖 Chatbot: I'm not a weather bot yet, but it looks like a great day! 🌤️")
        
        elif "help" in user_input:
            print("🤖 Chatbot: Sure! You can ask me about my name, the weather, or just say hello.")
        
        else:
            print("🤖 Chatbot: Hmm… I'm not sure about that. Could you rephrase?")

# Only run the chatbot if this file is executed directly
if __name__ == "__main__":
    chatbot()
