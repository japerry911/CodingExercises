"""
---Find Common Characters---
Given an array A of strings made only from lowercase letters, return a
list of all characters that show up in all strings within the list (including
duplicates).  For example, if a character occurs 3 times in all strings but not
4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
"""

from typing import List
import copy


def common_chars(A: List[str]) -> List[str]:
    master_char_dict = None
    first_run = True
    return_list = list()

    for string in A:
        sub_char_dict = dict()

        for char in string:
            if char not in sub_char_dict.keys():
                sub_char_dict[char] = 1
            else:
                sub_char_dict[char] += 1

        if first_run is True:
            master_char_dict = sub_char_dict
            first_run = False
        else:
            master_chars = copy.deepcopy(master_char_dict)
            for master_char in master_chars.keys():
                if master_char in sub_char_dict.keys():
                    if sub_char_dict[master_char] < master_char_dict[master_char]:
                        master_char_dict[master_char] = sub_char_dict[master_char]
                else:
                    del master_char_dict[master_char]

    for key, val in master_char_dict.items():
        for i in range(0, val):
            return_list.append(key)

    return return_list


if __name__ == "__main__":
    print(common_chars(["cool"]))
