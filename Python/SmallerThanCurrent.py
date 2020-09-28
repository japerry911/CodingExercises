"""
---How Many Numbers are Smaller than the Current Number---
Given the array nums, for each nums[i] find out how many numbers in the 
array are smaller than it. That is, for each nums[i] you have to count 
the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    return [len(list(filter(lambda y: y < x, nums))) for x in nums]
