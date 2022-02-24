"""
    https://leetcode.com/problems/maximum-product-subarray/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Using DP:
        # * State: Current Num: `i`
        #
        # * Logic: Let's Ignore the zeros for now.
        #
        # - Both '-ve' and '+ve' numbers are favorable
        # - '-ve's are favorable if they are in even count
        # - Also note that product will be maximum if we can take
        # product of all numbers in array, hence the product array
        # shall be bound to the array boundary (more specifically to nearest '0' boundary)
        # - To keep '-ve's on our side, we will maintain 2 products: `Min_prod` and `Max_prod`
        # - Note that a single '-ve' number will convert `Max_prod` to the `Min_prod` and similarly
        # a sngle '-ve' number will convert `Min_prod` to `Max_prod`
        # - Therefore, We will keep taking the maximum of `(Min_prod * num, Max_prod * num)` as `Max_prod`
        # Similarly `Min_prod = min(Max_prod * num, Min_Prod * num)`
        #
        # * Handling Zeros:
        # - Since a '0' will make our product '0', hence, we will have to restart the prod with
        # next number
        # - Therefore, the above relation will be modified a little to include the case of '0'
        # i.e. `Max_prod = max(num, num * Max_prod, num * Min_prod)`
        # and `Min_prod = min(num, num * Max_prod, num * Min_prod)`

        # Finally, the `ans` will be the maximum `Max_prod` encountered ever.

        max_prod = min_prod = ans = nums[0]

        # print(f"0: {nums[0]} {max_prod} {min_prod} {ans}")

        for i, num in enumerate(nums[1:], start=1):
            new_max = max_prod * num
            new_min = min_prod * num

            max_prod = max(num, new_max, new_min)
            min_prod = min(num, new_max, new_min)

            ans = max(ans, max_prod)

            # print(f"{i}: {nums[0]} {max_prod} {min_prod} {ans}")

        return ans

