"""
---Sort Array by Parity II---
Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even,
i is even.

You may return any answer array that satisfies this condition. 
"""


def sort_array_by_parity_ii(input_list: List[int]) -> List[int]:
    # declaring and initializing return_list with 0s adding to size of input_list,
    #  and indices for tracking both input_list and return_list current index
    return_list = list(map(lambda x: 0, [None] * len(input_list)))
    return_list_index = 0
    input_list_index = 0

    while len(input_list) > 0:
        # check if return_list_index is even or odd
        if return_list_index % 2 == 0:
            # check if input_list current index value is even as well, if so add it to return_list and
            #  pop it off input_list list and increment return_list_index & reset input_list_index to 0
            if input_list[input_list_index] % 2 == 0:
                return_list[return_list_index] = input_list.pop(
                    input_list_index)
                return_list_index += 1
                input_list_index = 0
            else:
                # if it is not even, then increment to next input_list value
                input_list_index += 1
        else:
            # check if input_list current index value is odd as well, if so add it to return_list and
            #  pop it off input_list list and increment return_list_index & reset input_list_index to 0
            if input_list[input_list_index] % 2 == 1:
                return_list[return_list_index] = input_list.pop(
                    input_list_index)
                return_list_index += 1
                input_list_index = 0
            else:
                # if it is not odd, then increment to next input_list value
                input_list_index += 1

    return return_list
