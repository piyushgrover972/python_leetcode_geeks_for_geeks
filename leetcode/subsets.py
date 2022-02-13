"""
    https://leetcode.com/problems/subsets/

    Tags: POTD; Recursion/BackTracking; Medium
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        # Create Power Set including set of size 0 and upto len(nums)
        for i in range(len(nums) + 1):
            ans.extend(self.choose(nums, i, []))

        return ans

    # Simple Recursive Combinations (not Permutations) generator; see the Problem: Combinations
    def choose(self, nums: List[int], k: int, combi: List[int]) -> List[List[int]]:

        ans = []

        if len(combi) < k:
            for i ,v in enumerate(nums):
                ans.extend(self.choose(nums[i + 1:], k, combi + [v]))

        else:
            return [combi]

        return ans