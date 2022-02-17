"""
    https://leetcode.com/problems/reverse-bits/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        if n:
            # Reverse the digits in 2^0 size set/group
            n = ((n & 0xAA_AA_AA_AA) >> 1) | ((n & 0x55_55_55_55) << 1)

            # Reverse the digits in 2^1 size set/group
            n = ((n & 0xCC_CC_CC_CC) >> 2) | ((n & 0x33_33_33_33) << 2)

            # Reverse the digits in 2^2 size set/group
            n = ((n & 0xF0_F0_F0_F0) >> 4) | ((n & 0x0F_0F_0F_0F) << 4)

            # Reverse the digits in 2^3 size set/group
            n = ((n & 0xFF_00_FF_00) >> 8) | ((n & 0x00_FF_00_FF) << 8)

            # Reverse the digits in 2^4 size set/group
            n = ((n & 0xFF_FF_00_00) >> 16) | ((n & 0x00_00_FF_FF) << 16)

        return n
