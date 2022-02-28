"""
    https://leetcode.com/problems/summary-ranges/

    Tags: POTD; Easy;
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        ans = []

        lo = 0
        hi = 1
        while hi < len(nums):
            if hi - lo == nums[hi] - nums[lo]:
                hi += 1

            else:
                if hi == lo + 1:
                    ans.append(str(nums[lo]))
                else:
                    ans.append(f"{nums[lo]}->{nums[hi - 1]}")

                lo = hi
                hi += 1

        if hi == lo + 1:
            ans.append(str(nums[lo]))
        elif hi > lo:
            ans.append(f"{nums[lo]}->{nums[hi - 1]}")

        return ans
