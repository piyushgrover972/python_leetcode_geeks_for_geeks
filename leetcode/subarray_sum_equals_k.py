"""
    https://leetcode.com/problems/subarray-sum-equals-k/

    Tags: POTD; Prefix Sum; HashMap; Medium
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0

        # HashMap to keep count of how many times a particular value of sum has occurred
        # Sum '0' has occurred once
        hmap = {0: 1}

        summ = 0
        for i in range(len(nums)):

            summ += nums[i]

            if summ - k in hmap:
                ans += hmap[summ - k]

            if summ in hmap:
                hmap[summ] += 1

            else:
                hmap[summ] = 1

            # print(f"{hmap} {ans}")

        return ans

