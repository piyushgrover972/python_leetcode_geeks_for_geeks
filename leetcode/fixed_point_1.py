"""
    https://leetcode.com/problems/fixed-point/

    Tags: Practice; Concepts; Algorithms; Binary-Search; Easy
"""

from typing import List


# TC: O(n), SC: O(1)
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, a in enumerate(arr):
            if i == a:
                return i
        return -1