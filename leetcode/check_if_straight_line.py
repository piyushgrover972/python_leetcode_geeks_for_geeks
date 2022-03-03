"""
    https://leetcode.com/problems/check-if-it-is-a-straight-line/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # Check the value of slope from the coordinate values is same for all pairs

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        for x, y in coordinates:

            if (y - y2) * (x - x1) != (y - y1) * (x - x2):
                return False

        return True
