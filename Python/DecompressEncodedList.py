"""
---Decompress Run-Length Encoded List---
We are given a list nums of integers representing a list compressed with 
run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] 
(with i >= 0).  For each such pair, there are freq elements with value val 
concatenated in a sublist. Concatenate all the sublists from left to right to 
generate the decompressed list.

Return the decompressed list.
"""


def decompress_rle_list(nums: List[int]) -> List[int]:
    # declare and initialize empty return list
    return_list = list()
    # declare and initialize to the first value in input list a variable that holds generate number
    generate_number = nums[0]

    # loop through input list and generate return_list, start from 1 due to generate number initializing
    for i in range(1, len(nums)):
        # if even, then store current number as generate_number
        if i % 2 == 0:
            generate_number = nums[i]
        # otherwise, create the current number generate_number times
        else:
            for r in range(0, generate_number):
                return_list.append(nums[i])

    return return_list
