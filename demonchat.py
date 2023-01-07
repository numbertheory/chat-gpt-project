doll_name = "Annabelle"

print("You are now chatting with " + doll_name +
      ". Type 'quit' to end the conversation.")

while True:
    message = input("> ")
    if message.lower() == "quit":
        print(doll_name + ": Goodbye!")
        break
    else:
        print(doll_name + ": I'm sorry, I didn't understand "
              "what you said. Could you repeat that?")
