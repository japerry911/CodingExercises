"""
---Running Sum 1D Array---
Given an array nums. We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


def running_sum(nums: List[int]) -> List[int]:
    # declare running sum return list
    running_sum_list = list()

    # calculate running sums and append running sums to running sum return list
    for i in range(0, len(nums)):
        current_running_sum = 0
        for r in range(0, i + 1):
            current_running_sum += nums[r]
        running_sum_list.append(current_running_sum)

    return running_sum_list
