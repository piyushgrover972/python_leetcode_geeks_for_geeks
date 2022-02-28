"""
    https://leetcode.com/problems/counting-bits/

    Tags: Dynamic programming; Bit Manipulation; Easy
"""

from typing import List


class Solution:
    def setbits(self, n: int):

        cnt = 0
        while n:
            n &= n - 1
            cnt += 1

        return cnt

    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(0, n + 1):
            ans.append(self.setbits(i))

        return ans
