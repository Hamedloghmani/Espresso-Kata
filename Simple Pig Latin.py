"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(sentence: str):
    # splitting the sentence into seperated words
    sentence = sentence.split()
    # moving the first letter to the end and adding 'ay' if the word isalpha(), leaving it unchanged otherwise
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in sentence])
