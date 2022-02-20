"""
    https://leetcode.com/problems/delete-and-earn/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List, Dict
import collections


class Solution:
    def __init__(self):
        self.dp_curr_sum = {}

    def deleteAndEarn(self, nums: List[int]) -> int:
        # Algorithm
        # Since, the order of choosing numbers is not fixed, we start with sorted array,
        # so that consecutive numbers can be at adjacent positions.
        #
        # Now,
        # If current and prev adjacent number are consecutive
        #   Choice 1: If we choose current,
        #       `dp_sum_1 = dp[i - 2] + cur_num`
        #   Choice 2: If we do not choose current,
        #       `dp_sum_2 = dp[i - 1]`
        # So we should go with the `max(dp_sum_1, dp_sum_2)`
        #
        # If current and prev adjacent number are not consecutive
        #   Then, `dp_sum = dp(i - 1) + cur_num`
        #
        # Since number can be repeated, we will keep the freq of each number
        # and if we choose a number, we will multiply it with its freq.

        # Calculate freq:
        counts = collections.Counter(nums)

        # print(counts)

        # Use DP (Top-Down) to solve
        return self.dp_max_sum(len(counts) - 1, sorted(counts), counts)

    def dp_max_sum(self, i: int, nums: List[int], freq: Dict[int, int]) -> int:

        if i == 0:
            self.dp_curr_sum[0] = nums[0] * freq[nums[0]]

        # We need `i = 1` base case, because recurrence relation accesses `i - 1` & `i - 2` as well,
        # which decays down to `1` and `0`
        elif i == 1:
            if nums[1] - 1 == nums[0]:
                self.dp_curr_sum[1] = max(nums[1] * freq[nums[1]], self.dp_max_sum(0, nums, freq))

            else:
                self.dp_curr_sum[1] = self.dp_max_sum(0, nums, freq) + nums[1] * freq[nums[1]]

        elif i not in self.dp_curr_sum:
            # Prev number is consecutive
            if nums[i - 1] == nums[i] - 1:
                # We either chose `(current + dp(i - 2))` Or, `dp(i - 1)`
                self.dp_curr_sum[i] = max(self.dp_max_sum(i - 2, nums, freq) + (nums[i] * freq[nums[i]]),
                                          self.dp_max_sum(i - 1, nums, freq))

            else:
                self.dp_curr_sum[i] = self.dp_max_sum(i - 1, nums, freq) + (nums[i] * freq[nums[i]])

        return self.dp_curr_sum[i]
