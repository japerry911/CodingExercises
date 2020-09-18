"""
---Three Consecutive Odds---
Given an integer array arr, return true if there are three 
consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""


def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    odd_counter = 0
    for element in arr:
        if element % 2 == 1:
            odd_counter += 1
        else:
            odd_counter = 0

        if odd_counter == 3:
            return True

    return False
