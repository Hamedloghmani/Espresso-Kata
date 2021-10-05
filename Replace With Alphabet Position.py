"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
"""
from string import ascii_lowercase

# First we have to create an indexed dictionary of the alphabet
alphabet = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(sentence: str):
    # Converting the sentence to lowercase
    sentence = sentence.lower()
    # Creating a list as the mapping of letters to numbers
    position_of_alphabet = list(alphabet[letter] for letter in sentence if letter in alphabet)
    # Creating the final string using space as the separator
    return ' '.join(position_of_alphabet)
