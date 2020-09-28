"""
---Subtract the Product and Sum of Digits of an Integer---
Given an integer number n, return the difference between the 
product of its digits and the sum of its digits. 
"""


def subtract_product_and_sum(n: int) -> int:
    return reduce(lambda acc, x: acc * int(x), str(n), 1) - sum(list(map(lambda x: int(x), str(n))))
