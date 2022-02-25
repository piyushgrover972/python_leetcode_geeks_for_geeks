"""
    https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

    Tags: Study Plan; Programming Skills; Easy
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + ((high % 2) or (low % 2))
