"""
---Max Product of List---
Given the array of integers nums, you will choose two 
different indices i and j of that array. Return the maximum 
value of (nums[i]-1)*(nums[j]-1).
"""


def max_product(nums: List[int]) -> int:
    # declare and initialize max product return value to 1
    return_value = 1

    # sort nums input list so that largest numbers are at the front
    nums.sort(reverse=True)

    # calculate return value by using the product of the first nums (subtract one from each before multiplying)
    return_value *= (nums[0] - 1) * (nums[1] - 1)

    return return_value
