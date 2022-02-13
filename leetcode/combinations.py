"""
    https://leetcode.com/problems/combinations/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Medium
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = self.choose(list(range(1, n + 1)), k, [])

        # print(ans)

        return ans

    def permute(self, values: List[int], k: int, permut: List[int]):

        ans = []

        # While the length of permut is less than reqd, keep recursing
        if len(permut) < k:
            for i, v in enumerate(values):
                # For subsequent recursion, skip the value already chosen at current position
                # and pass (a copy of) remaining values to choose from
                # Also, pass the (copy of) semi-complete permutation
                ans.extend(self.permute(values[:i] + values[i + 1:], k, permut + [v]))

        else:
            # The permutation is complete, return it
            return [permut]

        return ans

    # To understand Combinations, first understand the Permutations
    # The only diff here is that all the previously chosen values are not passed for successive recursions,
    # i.e. for successive choices
    def choose(self, values: List[int], k: int, combi: List[int]):

        ans = []
        if len(combi) < k:
            for i, v in enumerate(values):
                # All the values before `i` have already been chosen in previous recursion cycles.
                ans.extend(self.choose(values[i + 1:], k, combi + [v]))

        else:
            return [combi]

        return ans
