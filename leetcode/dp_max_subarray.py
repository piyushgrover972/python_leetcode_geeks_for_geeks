"""
    https://leetcode.com/problems/maximum-subarray/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Algo: Use DP
        # DP State: Current index
        # For each index, we have 2 choices:
        # 1. Choose cur num as part of last subarray
        # 2. Choose cur num to start new subarray
        # sum(i) in first case: sum(i - 1) + num
        # sum(i) in second case: num
        # Therefore, after every step: `dp_sum(i) = max(dp_sum(i - 1), 0) + num`
        # Base Case: dp_sum(0) = num[0]
        # Another step: Keep track of max sum encountered ever, and return the that maximum val `dp_sum(j)`

        max_sum = nums[0]
        summ = 0
        for i, num in enumerate(nums):
            summ = max(summ, 0) + num
            if max_sum < summ:
                max_sum = summ

        return max_sum
