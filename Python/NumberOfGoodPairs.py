"""
---Number of Good Pairs---
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""


def num_identical_pairs(nums: List[int]) -> int:
    # declare and initialize to 0 return pair count variable
    pair_count = 0

    # loop through the nums in nested for loop and calculate pair_count
    for i in range(0, len(nums)):
        for r in range(i + 1, len(nums)):
            if nums[i] == nums[r]:
                pair_count += 1

    return pair_count
