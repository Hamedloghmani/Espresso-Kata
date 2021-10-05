"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (like the name of this kata).
"""


def spin_words(text: str):
    split_text = text.split()
    final_string = ""
    # Splitting the sentence into seperated words
    for i in range(0, len(split_text)):
        if len(split_text[i]) >= 5:
            split_text[i] = split_text[i][::-1]
    # Checking the length of the word list to figure if we need to reconstruct the sentence
    if len(split_text) == 1:
        final_string = split_text[0]
    else:
        for i in range(0, len(split_text)):
            if i != len(split_text) - 1:
                final_string += split_text[i] + ' '
            else:
                # Because there is no need for extra space at the end of the sentence
                final_string += split_text[i]

    return final_string
