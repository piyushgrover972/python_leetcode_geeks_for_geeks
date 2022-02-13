"""
    https://leetcode.com/problems/permutations/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Medium
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permutations(nums, len(nums), [])

    # This function calculates nPk [n! / (n - k)!],
    # i.e. the number of permutations of size `k` from an input list of size `n`
    def permutations(self, values: List[int], k: int, permut: List[int]) -> List[List[int]]:

        ans = []

        # While the length of permut is less than reqd, keep recursing
        if len(permut) < k:
            for i, v in enumerate(values):
                # For subsequent recursion, skip the value already chosen at current position
                # and pass (a copy of) remaining values to choose from
                # Also, pass the (copy of) semi-complete permutation
                ans.extend(self.permutations(values[:i] + values[i + 1:], k, permut + [v]))
        else:
            # The permutation is complete, return it
            return [permut]

        return ans
