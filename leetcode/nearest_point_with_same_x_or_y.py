"""
    https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        dist = None
        idx = -1
        for i, point in enumerate(points):
            if point[0] == x:
                if dist is not None:
                    if dist > abs(y - point[1]):
                        dist = abs(y - point[1])
                        idx = i
                else:
                    dist = abs(y - point[1])
                    idx = i

            if point[1] == y:
                if dist is not None:
                    if dist > abs(x - point[0]):
                        dist = abs(x - point[0])
                        idx = i
                else:
                    dist = abs(x - point[0])
                    idx = i

        return idx
