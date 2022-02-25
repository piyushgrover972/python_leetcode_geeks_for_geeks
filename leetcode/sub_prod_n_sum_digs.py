"""
    https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

    Tags: Study Plan; Programming Skills; Easy
"""

import functools


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = sum(map(int, str(n)))
        p = functools.reduce(lambda a, e: a * e, map(int, str(n)))

        return p - s
