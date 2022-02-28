"""
    https://leetcode.com/problems/remove-covered-intervals/

    Tags: POTD; Medium; Sorting
"""

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        iv = intervals
        rem = set()
        for i in range(len(iv)):
            for j in range(i + 1, len(iv)):
                if j not in rem and i not in rem:
                    if iv[i][0] <= iv[j][0] and iv[i][1] >= iv[j][1]:
                        rem.add(j)
                    elif iv[j][0] <= iv[i][0] and iv[j][1] >= iv[i][1]:
                        rem.add(i)

        return len(iv) - len(rem)
