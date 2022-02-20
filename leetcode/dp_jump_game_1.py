"""
    https://leetcode.com/problems/jump-game/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        # Start from last index
        # `cur = len(nums) - 1`
        # Check in a loop
        # Is `cur` index reachable from `prev` index?
        #   - Yes:
        #       - Set `dp_reachable_from[prev] = True`
        #       - `Recursive DP call with `cur <= prev`
        #   - No:
        #       - Set `dp_reachable_from[prev] = False`
        #       - prev -= 1
        #

        dp_reach_from = {}

        def dp_reachable(to_idx: int, from_idx: int):

            prev = to_idx - 1

            while prev >= from_idx:

                if prev + nums[prev] >= to_idx:
                    dp_reach_from[prev] = True

                    return dp_reachable(prev, from_idx)

                else:
                    dp_reach_from[prev] = False
                    prev -= 1

            return dp_reach_from[from_idx]

        return dp_reachable(len(nums) - 1, 0)
