"""
    https://leetcode.com/problems/combination-sum-iii/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Medium
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # Create a list of nums to choose fromx
        return self.combinations(list(range(1, 10)), [], n, k)

    def combinations(self, nums: List[int], combi: List[int], s: int, k: int):

        ans = []

        # If only one slot is    remaining, we do not need further recursion...
        if len(combi) == k - 1:
            # ... just Check if the remaining sum is present in the `nums` as a single number
            if s in nums:
                return [combi + [s]]
            else:
                return None

        # Algorithm
        for i, v in enumerate(nums):
            remaining_sum = s - v

            # Since we have a sorted the array of nums to chose from, hence, to avoid unnecessary recursive calls,
            # check if remaining sum is greater than the current value
            if remaining_sum > v:

                # Since, we can't have duplicates, nor can we have permutations of already chosen combinations,
                # We will pass only the remaining array to the next recursion.
                remaining_list_to_chose_from = nums[i + 1:]

                # Append the current value to the combination
                new_combi = combi + [v]

                final_combi = self.combinations(remaining_list_to_chose_from, new_combi, remaining_sum, k)

                if final_combi is not None:
                    ans.extend(final_combi)

            else:
                break

        return ans
