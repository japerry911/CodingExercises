"""
---Create Target Array in the Given Order---
Given two arrays of integers nums and index. Your task is to create 
target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] 
the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and 
index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""


def create_target_array(nums: List[int], index: List[int]) -> List[int]:
    # declare and initialize to empty list a return list variable
    target_list = list()

    # loop through the two input arrays and fill the target_list
    for i in range(0, len(nums)):
        target_list.insert(index[i], nums[i])

    return target_list
