"""
    https://leetcode.com/problems/find-anagram-mappings/

    Tags: Google Assessment; HashMap; Easy;
"""

from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = {}
        l = []
        for i, n in enumerate(nums2):
            d[n] = i

        for n in nums1:
            l.append(d[n])

        return l
