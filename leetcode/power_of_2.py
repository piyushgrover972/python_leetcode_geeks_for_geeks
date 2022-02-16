"""
    https://leetcode.com/problems/power-of-two/

    Tags: Practice; Concepts; Algorithms; Bit Manipulation; Easy
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Clear the first set ('1') LSB, if the number reduces to `0`, it is power of 2
        # Also discard numbers <= 0
        return n > 0 and not (n & n - 1)