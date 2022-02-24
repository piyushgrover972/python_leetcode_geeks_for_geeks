"""
    https://leetcode.com/problems/pascals-triangle/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""

from typing import List


class Solution:
    def __init__(self):
        self.cache = [[1], [1, 1]]

        for r in range(2, 34):
            new = [1, 1]

            lim = r // 2
            for i in range(1, lim + 1):
                new.insert(i, self.cache[r - 1][i - 1] + self.cache[r - 1][i])
                if i != r - i:
                    new.insert(i, self.cache[r - 1][i - 1] + self.cache[r - 1][i])

            self.cache.append(new)

    def getRow(self, rowIndex: int) -> List[int]:

        return self.cache[rowIndex]
