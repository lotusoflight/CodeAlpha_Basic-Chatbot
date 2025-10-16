import random

def get_bot_response(user_input):
    user_input = user_input.strip().lower()

    responses = {
        "hello": "Hello! ",
        "hi": "Hi there!",
        "how are you": "I'm doing great! How about you?",
        "bye": "Goodbye! ",
        "what is your name": "I'm a simple chatbot created to chat with you.",
        "who are you": "I'm your friendly chatbot assistant.",
        "thank you": "You're welcome! ",
        "thanks": "No problem!",
        "help": "Sure, I'm here to help. What do you need?",
    }

  
    if user_input in responses:
        return responses[user_input]

    fallback_responses = [
        "I'm not sure I understand. Can you try saying that differently?",
        "Hmm, interesting! Tell me more.",
        "Let's keep chatting. What else would you like to talk about?",
    ]

    return random.choice(fallback_responses)

def start_chatbot():
    print(" Chatbot: Hello! I'm here to chat. Type 'bye' to exit.")

    while True:
        user_input = input(" You: ")
        response = get_bot_response(user_input)
        print(" Chatbot:", response)

        if user_input.strip().lower() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    start_chatbot()
