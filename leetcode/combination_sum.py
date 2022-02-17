"""
    https://leetcode.com/problems/combination-sum/

    Tags: POTD; Medium; Algorithms; Recursion/Backtracking
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Minor Optimization: Not Needed, but Good to have
        # Filter out all the numbers greater than the 'target'
        candidates = filter(lambda a: a <= target, candidates)

        return self.combinations(list(candidates), [], target)

    def combinations(self, nums: List[int], combi: List[int], s: int):

        # print(f"<< {nums=}, {combi=}, {s=} >>")
        ans = []

        # If the sum reduces to '0', it means, we have found a combination of numbers adding upto 'target'
        if s == 0:
            return [combi]
        # If the sum becomes -ve, it means, current combination can never add upto the 'target', hence return 'None'
        elif s < 0:
            return None

        # Algorithm:
        # 1. Choose all the number one by one and keep calling recursively, with the current and the following
        # numbers in the array
        # 2. Add the chosen number to the sequence and pass on to next recursive call
        # 3. Decrease the sum by the number chosen
        for i, v in enumerate(nums):

            # Keep current number too, as it can be used again unlimitedly
            # Do not keep previous numbers to avoid duplicate combinations
            # (i.e. permutations of already chosen combinations)
            remaining_nums_to_choose_from = nums[i:]

            new_combi = combi + [v]
            remaining_sum = s - v

            final_combi = self.combinations(remaining_nums_to_choose_from, new_combi, remaining_sum)

            if final_combi is not None:
                ans.extend(final_combi)

        return ans
