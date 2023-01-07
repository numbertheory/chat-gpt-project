import random
import json

# Load the JSON file
with open('doll_responses.json', 'r') as f:
    data = json.load(f)


def choose_random_string():
    # Human fix: This combines answers 2 and 4 to make it
    # a bit more efficient in handling the data and not
    # requiring the script to provide the list.
    # Get the list of responses
    responses = data['responses']
    return random.choice(responses)


doll_name = "Annabelle"

print("You are now chatting with " + doll_name +
      ". Type 'quit' to end the conversation.")

while True:
    message = input("> ")
    if message.lower() == "quit":
        print(doll_name + ": Goodbye!")
        break
    else:
        print(doll_name + ": " + choose_random_string())
