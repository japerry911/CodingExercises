"""
---Number of Steps to Zero---
Given a non-negative integer num, return the number of steps 
to reduce it to zero. If the current number is even, you have 
to divide it by 2, otherwise, you have to subtract 1 from it
"""


def number_of_steps(num: int) -> int:
    # declare and initialize to 0 return steps
    steps = 0

    # loop through until num input is 0 and follow rules to get it to 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1

        steps += 1

    return steps
