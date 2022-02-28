"""
    https://leetcode.com/problems/random-pick-with-weight/

    Tags: Google; Medium
"""

import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.cum = [w[0]]

        for wt in w[1:]:
            self.cum.append(self.cum[-1] + wt)

    def bs(self, n: int):
        l, h = 0, len(self.cum) - 1

        while l <= h:
            m = (l + h) // 2

            if self.cum[m] > n:
                if not m or self.cum[m - 1] < n:
                    return m
                else:
                    h = m - 1

            elif self.cum[m] < n:
                if m == len(self.cum) - 1 or self.cum[m + 1] > n:
                    return m + 1
                else:
                    l = m + 1

            else:
                return m

    def pickIndex(self) -> int:

        pick = random.randint(1, self.cum[-1])

        print(f"{pick}", end=" ")

        return self.bs(pick)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()