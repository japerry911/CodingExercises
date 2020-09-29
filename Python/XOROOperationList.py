"""
---XOR Operating in an Array---
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""


from functools import reduce


def xor_operation(n: int, start: int) -> int:
    return reduce(lambda acc, x: acc ^ x, list(range(start, (n * 2) + start, 2)))
