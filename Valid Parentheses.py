"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
 The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string: str):
    counter = 0
    for char in string:
        # if the counter goes below zero at any point it means we have more ) than (, so the output is False
        if counter < 0:
            return False
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
    # if the counter equals to zero it means we had the right order
    return True if counter == 0 else False
