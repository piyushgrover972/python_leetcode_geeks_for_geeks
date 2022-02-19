"""
    https://leetcode.com/contest/biweekly-contest-72/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

    Tags: BiWeekly-Contest_72; Maths;
"""

from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if num % 3 == 0:
            n = num // 3
            return [n - 1, n, n + 1]
        else:
            return []
