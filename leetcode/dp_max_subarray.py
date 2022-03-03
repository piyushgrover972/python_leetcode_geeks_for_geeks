"""
    https://leetcode.com/problems/maximum-subarray/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum = nums[0]
        cursum = maxsum

        # print(f"{cursum} {maxsum}")
        for num in nums[1:]:

            # We have 2 choices:
            # We can restart the `sum` from current `num`
            # Or, we can continue prev `sum` and add current `num` to it.
            cursum = max(num, num + cursum)

            # Keep track of maxsum ever encountered
            if cursum > maxsum:
                maxsum = cursum

            # print(f"{cursum} {maxsum}")

        return maxsum

