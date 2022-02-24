"""
    https://leetcode.com/problems/maximum-sum-circular-subarray/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        # Since the array is circular, the Max sub array can either be a regular sub array
        # Or, may start towards the end and end towards the start, i.e. wrap around.

        # For first case, we can use the same logic to find Max subarray as for a regular array
        # For second case, since the Max array is wrapping around, the Min Array shall be a regular array
        # Hence, find the Min SubArray sum and subtract it from the Total Array Sum

        # Finally, return the maximum of the 2.

        # Edge Case: If the Array Total and Min SubArray are same, it means, all nums < 0
        # In that case, simply return the answer for the first case.

        sum_mx = sum_mn = max_sum = min_sum = nums[0]

        for num in nums[1:]:
            sum_mx = max(sum_mx, 0) + num
            if max_sum < sum_mx:
                max_sum = sum_mx

            sum_mn = min(sum_mn, 0) + num
            if min_sum > sum_mn:
                min_sum = sum_mn

        total = sum(nums)

        if total != min_sum:
            max_sum = max(sum(nums) - min_sum, max_sum)

        return max_sum
