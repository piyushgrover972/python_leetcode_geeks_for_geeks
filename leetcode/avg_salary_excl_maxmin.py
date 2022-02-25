"""
    https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return round((sum(salary) - sum([max(salary), min(salary)])) / (len(salary) - 2), 5)