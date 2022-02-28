"""
    https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

    Tags: Study Plan; Programming Skills; Easy
"""

import collections


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter(s2)

        if cnt1 == cnt2:
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1

                if diff > 2:
                    return False

            return True if diff in {0, 2} else False

        return False
