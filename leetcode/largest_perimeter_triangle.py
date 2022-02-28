"""
    https://leetcode.com/problems/largest-perimeter-triangle/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        i = len(nums) - 1
        while i >= 2:
            edge_sum = nums[i - 1] + nums[i - 2]

            if edge_sum > nums[i]:
                return edge_sum + nums[i]

            i -= 1

        return 0
