def chatbot():
    print("Hello! I'm Chatbot. Type 'quit' to exit the conversation.")
    
    while True:
        
        user_input = input("You: ").lower()
        
        
        if user_input == 'quit':
            print("Goodbye! Have a nice day!")
            break
        
        
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm fine what about you?")

        elif 'I am fine' in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")

        elif 'your name' in user_input:
            print("Chatbot: I'm Chatbot I can assist you")
        
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif 'weather' in user_input:
            print("Chatbot: Results for Kakinada, Andhra Pradesh Partly Cloudy 28°C°F Precipitation 10% Humidity 63% Wind 18 km/h Weather Sunday Partly Cloudy TemperaturePrecipitationWind")
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you ask something else?")


chatbot()
