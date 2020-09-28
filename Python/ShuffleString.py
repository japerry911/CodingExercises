"""
---Shuffle String---
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position 
moves to indices[i] in the shuffled string.

Return the shuffled string.
"""


def restore_string(s: str, indices: List[int]) -> str:
    # declare and initialize to list filled with zeroes a return string list
    return_string = list(map(lambda x: "", [None] * len(indices)))

    # loop through indices and input string and form the return_string list
    for i in range(0, len(indices)):
        return_string[indices[i]] = s[i]

    # return the return_string list joined into a string
    return "".join(return_string)
