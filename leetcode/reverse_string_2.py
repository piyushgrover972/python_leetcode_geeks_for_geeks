"""
    https://leetcode.com/problems/reverse-string/

    Tags: Concepts; Algorithms; Two Pointers; Easy
"""
from typing import List


class Solution:
    """
    Reverse string using "Two Pointers"
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.revs(s, 0)

    def revs(self, s: List[str], n: int):
        if n == len(s) // 2:
            return

        s[n], s[len(s) - 1 - n] = s[len(s) - 1 - n], s[n]
        self.revs(s, n + 1)
