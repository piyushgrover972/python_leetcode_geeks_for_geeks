"""
    https://leetcode.com/contest/weekly-contest-282/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

    Tags: Weekly-Contest_282; String; Medium
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(t)

        ops = 0

        for key in range(ord('a'), ord('z') + 1):
            # Counter is like a Default Dict, so it will return '0' for non-existent keys
            ops += abs(freq_t[chr(key)] - freq_s[chr(key)])

        return ops
