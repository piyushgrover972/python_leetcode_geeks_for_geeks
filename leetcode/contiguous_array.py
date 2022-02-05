"""
    https://leetcode.com/problems/contiguous-array/

    Tags: POTD; Concepts; Algorithms; Two Pointers, Medium
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0

        hashmap = {0: [-1]}

        for idx ,num in enumerate(nums):
            count += 1 if num else -1
            if count in hashmap:
                hashmap[count].append(idx)
            else:
                hashmap[count] = [idx]

        for k in hashmap:
            hashmap[k] = hashmap[k][-1] - hashmap[k][0]

        return max(hashmap.values())