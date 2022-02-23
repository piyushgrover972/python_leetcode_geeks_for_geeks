"""
    https://leetcode.com/problems/fixed-point/

    Tags: Practice; Concepts; Algorithms; Binary-Search; Easy
"""

from typing import List


# TC: O(log n), SC: O(log n) due to Recursion
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        if arr[0] > 0 or arr[-1] < len(arr) - 1:
            return -1

        return self.bs(arr)

    # Do Binary Search
    def bs(self, arr: List[int]) -> int:

        hi, lo = len(arr) - 1, 0

        while lo <= hi:
            mid = (lo + hi) // 2
            a = arr[mid]

            if a == mid:
                # Try for a lower index of match
                lower = self.bs(arr[:mid])
                return mid if lower == -1 else lower

            elif a < mid:
                lo = mid + 1

            else:
                hi = mid - 1

        return -1