"""
    https://leetcode.com/problems/house-robber-ii/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # Forget circular arrangement, and think linearly...

        # DP State: Current House `i`

        # Recurrence Relation:
        # Decision: Rob Current House / Not Rob Current House
        # Money if Rob Current house : `dp(i - 2) + money[i]` i.e. Whatever we robbed till second previous house + current money
        # Money if NOT Rob Current house : `dp(i - 1)` i.e. Whatever we had till last house
        # Hence `dp(i) = max(dp(i - 1), dp(i - 2) + money[i])`

        # Since houses are circularly arranged, i.e. First and Last cannot be robbed together, we do DP twice:
        #
        # 1. Remove last house from input array in first iteration
        # 2. Remove first house from input array in second iteration
        #
        # Now, Return the max money robbed out of both iterations

        # Edge case
        if len(nums) == 1:
            return nums[0]

        def dp_max_money(i: int, nums: List[int]):

            nonlocal dp_money

            if i == 0:
                dp_money[i] = nums[0]

            elif i == 1:
                dp_money[i] = max(nums[0], nums[1])

            elif i not in dp_money:
                dp_money[i] = max(dp_max_money(i - 1, nums), nums[i] + dp_max_money(i - 2, nums))

            return dp_money[i]

        # Iteration 1, Remove Last house
        dp_money = {}
        max_money1 = dp_max_money(len(nums) - 2, nums[:-1])

        # Iteration 2 Remove First House
        dp_money = {}
        max_money2 = dp_max_money(len(nums) - 2, nums[1:])

        # print(max_money1, max_money2)

        return max(max_money1, max_money2)
