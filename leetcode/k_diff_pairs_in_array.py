"""
    https://leetcode.com/problems/k-diff-pairs-in-an-array/

    Tags: POTD; Array; HashMap
"""

from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        count = 0
        visited = set()
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
                count += (num + k in nums_set) + (num - k in nums_set)
            elif k == 0 and num not in visited:
                count += 1
                visited.add(num)

        return count
