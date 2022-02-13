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
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]