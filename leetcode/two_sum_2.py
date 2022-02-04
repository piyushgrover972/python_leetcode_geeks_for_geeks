"""
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List, Optional

class Solution:

    def binsearch(self, nums: List[int], n: int) -> Optional[int]:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == n:
                return mid
            elif nums[mid] > n:
                hi = mid - 1
            else:
                lo = mid + 1

        return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0

        lenn = len(numbers)

        while i < lenn:
            second = self.binsearch(numbers[i + 1:], target - numbers[i])

            if second is not None:
                return [i + 1, i + 1 + second + 1]

            else:
                i += 1

            while i < lenn and numbers[i - 1] == numbers[i]:
                i += 1


