"""
    https://leetcode.com/problems/maximum-product-subarray/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Keep multiplying the numbers
        # If the product is `0`, set the product to `num`
        # Keep noting the `maxprod` ever encountered

        # If the number of -ve are even, we will get the max prod.
        # If there are lots of zeros, the above algo, will try to
        # calculate the global maximum product among the local non-zero subarrays.

        # To handle the case of odd -ve's, Run the same logic again, in reverse on the array
        # This will take into account the large -ve numbers at the end.

        # At the end, return the max of both the iterations.

        if len(nums) == 1:
            return nums[0]

        maxprod_1 = prod = nums[0]

        for num in nums[1:]:
            if prod:
                prod *= num
            else:
                prod = num

            if maxprod_1 < prod:
                maxprod_1 = prod

        maxprod_2 = prod = nums[-1]

        for num in nums[-2::-1]:
            if prod:
                prod *= num
            else:
                prod = num

            if maxprod_2 < prod:
                maxprod_2 = prod

        return max(maxprod_1, maxprod_2)
