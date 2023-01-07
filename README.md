# chat-gpt-project

This project is an experiment to see how far I can get with using just [ChatGPT](https://chat.openai.com/chat) to generate both code and ideas to create a project.

## Prompts

These are the prompts I used to generate the code for this project.

1. Create a python program where I can chat with a demonic doll. [Answer](answers/answer1.md)
2. What are some reactions that a demonic doll would have when chatting with a human? [Answer](answers/answer2.md)
3. Make a python function which returns a random choice from a list of strings. [Answer](answers/answer3.md)
4. Create a JSON file of the doll answers that you provided. [Answer](answers/answer4.md)
5. How would I make the script know if a question had been asked? [Answer](answers/answer5.md)
6. Create some new responses for the demon doll to provide when a question is posed. The answers should be creepy and some of them should reference hell, Satan, or the Apocalypse. [Answer](answers/answer6.md)

The raw answers to these prompts will be listed in the [answers/](answers/) folder in this repo.

## Rules

Some of the rules I'm setting for myself here:

1. Only include ideas that are provided as answers from prompts.
2. Correcting code to make it workable is fine, with comments.
3. Adding to the requirements.txt file to make imports work is fine, without comments. 
4. Correcting code for formatting, (i.e. flake8) is also fine, no comments needed in that case.
5. All answers will be provided in the answers/ folder, but maybe not used.


## Installation and runnning

Requirements can be installed via requirements.txt. Only requirements specified by imports suggested
by ChatGPT, with the exception of Flake8, will be added. Activate a virtual environment and install:

```
pip install -r requirements.txt
```

For `nltk`, you'll need to download some additional content, not part of the package. 
Run this command to download the current version (in the same virtual environment you installed the requirements):

```
python3 -c "import nltk; nltk.download('averaged_perceptron_tagger'); nltk.download('punkt')"
```

Finally, run the script and chat with Annabelle:

```
python3 demonchat.py
```
