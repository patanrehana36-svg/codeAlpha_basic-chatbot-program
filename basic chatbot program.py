while True:
    msg = input("You: ").lower()

    if msg == "hello":
        print("Bot: Hi!")
    elif msg == "how are you":
        print("Bot: I am fine.")
    elif msg == "what is your name":
        print("Bot: I am a Python Chatbot.")
    elif msg == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")