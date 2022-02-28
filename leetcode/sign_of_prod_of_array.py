"""
    https://leetcode.com/problems/sign-of-the-product-of-an-array/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negs = 0

        for n in nums:
            if n == 0:
                return 0

            negs += n < 0

        return -1 if negs % 2 else 1
