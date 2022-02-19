"""
    https://leetcode.com/contest/biweekly-contest-72/problems/count-equal-and-divisible-pairs-in-an-array/

    Tags: BiWeekly-Contest_72; Brute-Force;
"""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        ans = 0

        if len(set(nums)) == len(nums):
            return 0

        hmap = {}

        for i, n in enumerate(nums):
            if n in hmap:
                hmap[n].append(i)
            else:
                hmap[n] = [i]

        # print(hmap)
        for key in hmap:
            for idx, i in enumerate(hmap[key]):
                for j in hmap[key][idx + 1:]:
                    if (i * j) % k == 0:
                        # print(f"< {i}, {j} >")
                        ans += 1

        return ans
