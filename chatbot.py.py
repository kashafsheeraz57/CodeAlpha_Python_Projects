# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    
    elif user_input == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand."


print("===== SIMPLE CHATBOT =====")
print("Type 'bye' to exit the chatbot.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break
    with open("chat_log.txt","a") as file:
        file.write(f"You: {user_input}\n")
        file.write(f"Bot: {response}\n")
