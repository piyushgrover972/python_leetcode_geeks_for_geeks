"""
    https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        d = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] != arr[i - 1] + d:
                return False

        return True
