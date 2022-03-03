"""
    https://leetcode.com/problems/arithmetic-slices/

    Tags: POTD; Medium; Dynamic Programming
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        total = 0
        run = 0
        d = nums[1] - nums[0]

        i = 2
        while i < len(nums):

            if d == nums[i] - nums[i - 1]:
                run += 1
                total += run

            else:
                run = 0
                d = nums[i] - nums[i - 1]

            # print(nums[i], run, total)

            i += 1

        return total
