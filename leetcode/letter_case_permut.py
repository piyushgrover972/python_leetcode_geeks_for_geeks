"""
    https://leetcode.com/problems/letter-case-permutation/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Medium
"""

from typing import List

from string import ascii_lowercase, ascii_uppercase


alphabet = set(ascii_lowercase) | set(ascii_uppercase)


class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:

        ans = self.permute(s, 0)

        return ans

    def permute(self, letters: str, idx: int) -> List[str]:

        ans = []

        # This permutation is done !!
        if idx == len(letters):
            return [letters]

        # Permute the current char ...
        l = letters[idx]

        # ... if it is an alphabet
        if l in alphabet:

            # Recurse further once with lower and then with upper case of the current char
            # i.e. find the permutations of remaining string with current char
            ans.extend(self.permute(letters[:idx] + l.lower() + letters[idx + 1:], idx + 1))
            ans.extend(self.permute(letters[:idx] + l.upper() + letters[idx + 1:], idx + 1))

        # ... else, just go on with next recusrion step, without changing current char
        else:
            ans.extend(self.permute(letters, idx + 1))

        # print(f"<< {ans=}, {l=}, {idx=} >>")

        return ans
