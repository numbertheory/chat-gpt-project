# chat-gpt-project

This project is an experiment to see how far I can get with using just [ChatGPT](https://chat.openai.com/chat) to generate both code and ideas to create a project.

## Prompts

These are the prompts I used to generate the code for this project.

1. Create a python program where I can chat with a demonic doll.
2. What are some reactions that a demonic doll would have when chatting with a human?

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

To run:

```
python3 demonchat.py
```
