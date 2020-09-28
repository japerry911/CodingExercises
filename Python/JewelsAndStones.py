"""
---Jewels and Stones---
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of 
stone you have.  You want to know how many of the stones you have are also 
jewels.

The letters in J are guaranteed distinct, and all characters in J and S are 
letters. Letters are case sensitive, so "a" is considered a different type of 
stone from "A".
"""


def num_jewels_in_stones(j: str, s: str) -> int:
    # return the reduced stones to jewels count
    return reduce(lambda acc, c: acc + 1 if c in j else acc + 0, s, 0)
