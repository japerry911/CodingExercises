"""
---Reverse String---
Write a function that reverses a string. The input string is given as an 
array of characters char[].

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


def reverse_string(s) -> None:
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    # s.reverse()
    # print(s)


if __name__ == "__main__":
    reverse_string(["h", "e", "l", "l", "o"])
