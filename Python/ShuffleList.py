"""
---Shuffle List---
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


def shuffle(input_list: List[int], n: int) -> List[int]:
    # declare shuffled return list, x's list, and y's list
    shuffled_list = list()
    xs_list = [num for idx, num in enumerate(input_list) if idx < n]
    ys_list = [num for idx, num in enumerate(input_list) if idx >= n]

    # loop through the xs_list and ys_list and create shuffled_list
    for i in range(0, n):
        shuffled_list.append(xs_list[i])
        shuffled_list.append(ys_list[i])

    return shuffled_list
