"""
    https://leetcode.com/problems/move-zeroes/
"""
from typing import List, Tuple

ZERO = 0
NONZERO = 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        dest = -1

        while i < len(nums):
            if dest == -1:
                if nums[i] == 0:
                    dest = i

            else:
                if nums[i] != 0:
                    nums[dest] = nums[i]
                    dest += 1

            i += 1

        if dest == -1:
            return

        while dest < len(nums):
            nums[dest] = 0
            dest += 1