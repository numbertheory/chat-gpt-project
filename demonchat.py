import random
import json
import nltk

# Load the JSON file
with open('doll_responses.json', 'r') as f:
    data = json.load(f)


def is_question(message):
    # Tokenize the message into a list of words
    words = nltk.word_tokenize(message)

    # Part-of-speech tag the words
    tagged_words = nltk.pos_tag(words)

    # Check if the first word is a question word
    if tagged_words[0][1] in ['WDT', 'WP', 'WP$', 'WRB']:
        return True

    # Check if the last word is a question mark
    if tagged_words[-1][0] == '?':
        return True

    # Check if the first word is a pronoun and the second word is a verb
    if tagged_words[0][1] in ['PRP'] and tagged_words[1][1] in ['VBZ', 'VBP']:
        return True

    # If none of the above conditions are met, return False
    return False


def choose_random_string(message):
    # Human fix: This combines answers 2 and 4 to make it
    # a bit more efficient in handling the data and not
    # requiring the script to provide the list.
    # Get the list of responses
    # Human fix: This if/then logic and structure of the
    # doll_responses file is human intervention.
    if is_question(message):
        responses = data['questions']
    else:
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
        print(doll_name + ": " + choose_random_string(message))
