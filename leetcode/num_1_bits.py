"""
    https://leetcode.com/problems/number-of-1-bits/submissions/

    Tags: Practice; Concepts; Algorithms; Bit Manipulation; Easy
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n:
            # Keep clearing first '1' LSB
            n &= n - 1
            cnt += 1

        return cnt