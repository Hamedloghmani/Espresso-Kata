"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of
items without any elements with the same value next to each other and preserving the original order of elements.
For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    # Check if the iterable is empty
    if len(iterable) == 0:
        return []
    # First item of the iterable always exists in the final answer
    final_list = [iterable[0], ]
    # If an item is equal to its previous neighbour in the iterable, we pass and append it to the final answer otherwise
    for i in range(1, len(iterable)):
        if iterable[i] != iterable[i-1]:
            final_list.append(iterable[i])

    return final_list
