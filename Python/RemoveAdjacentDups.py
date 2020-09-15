"""
---Remove All Adjacent Duplicates  in String---
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""


def removeDuplicates(S: str) -> str:
    i = 1
    previous_value = S[0]
    beginning_index = 0
    adjacent_bool = False

    while i < len(S):
        if S[i] == previous_value:
            adjacent_bool = True
        else:
            if adjacent_bool is True:
                S = S[0: beginning_index:] + S[i::]
                i = 0
                adjacent_bool = False

            previous_value = S[i]
            beginning_index = i

        i += 1

    if adjacent_bool is True:
        if beginning_index == 0:
            S = S[0]
        else:
            S = S[0: beginning_index:] + S[i::]

    return S


if __name__ == "__main__":
    print(removeDuplicates("aaaaaaaa"))
