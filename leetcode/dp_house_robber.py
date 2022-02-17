"""
    https://leetcode.com/problems/house-robber/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


class Solution:
    def __init__(self):
        self.dp_money = {}

    def rob(self, nums: List[int]) -> int:

        # If there is one option only
        if len(nums) == 1:
            return nums[0]

        # If there are 2 houses only
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Base Case of the DP Recurrence Relation
        self.dp_money[0] = nums[0]
        self.dp_money[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # The DP Recurrence Relation:
            # At house `i`, you can either rob it, that means, following the constraints, you will have
            # money = `nums[i] + dp_money[i - 2]` (Since you can't rob house `i - 1`)
            # If you don't rob it, you will have whatever money you had before, i.e. at house `i - 1`
            # Our target is to find the max money we can make from either cases.
            self.dp_money[i] = max(self.dp_money[i - 1], self.dp_money[i - 2] + nums[i])

        # Return the amount if money you had at the last house.
        return self.dp_money[len(nums) - 1]
