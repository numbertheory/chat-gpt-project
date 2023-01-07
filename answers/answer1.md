## Prompt
Create a python program where I can chat with a demonic doll.

## Answer

Sure! Here is a basic example of a Python program that allows you to chat with a demonic doll. This program uses the input function to get user input, and the print function to display the doll's responses.

```python
doll_name = "Annabelle"

print("You are now chatting with " + doll_name + ". Type 'quit' to end the conversation.")

while True:
  message = input("> ")
  if message.lower() == "quit":
    print(doll_name + ": Goodbye!")
    break
  else:
    print(doll_name + ": I'm sorry, I didn't understand what you said. Could you repeat that?")
```

This program will continue running until the user types the word "quit", at which point the loop will break and the program will end. You can customize the behavior of the doll by adding additional logic to the loop. For example, you could have the doll respond to certain keywords or phrases, or you could have it generate random responses. Let me know if you have any questions or if you'd like further assistance.