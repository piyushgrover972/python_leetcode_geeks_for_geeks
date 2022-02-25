"""
    https://leetcode.com/problems/compare-version-numbers/

    Tags: POTD; Medium
"""

from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))

        ans = 0
        for vn1, vn2 in zip_longest(v1, v2, fillvalue=0):
            if vn1 > vn2:
                ans = 1
            elif vn1 < vn2:
                ans = -1

            if ans:
                break

        return ans
