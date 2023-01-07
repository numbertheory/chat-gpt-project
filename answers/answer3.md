## Prompt
Make a python function which returns a random choice from a list of strings.

## Answer
Sure! Here is a Python function that takes a list of strings as an argument and returns a random element from the list:

```python
import random

def choose_random_string(string_list):
  return random.choice(string_list)
```

This function uses the random.choice function from the Python random module to select a random element from the list. To use this function, you would pass a list of strings as an argument when you call it. For example:

```python
string_list = ['apple', 'banana', 'orange']

random_string = choose_random_string(string_list)
print(random_string)
```

This would output one of the three strings in string_list at random (either 'apple', 'banana', or 'orange'). Let me know if you have any questions or if you'd like further assistance.