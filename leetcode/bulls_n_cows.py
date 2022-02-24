"""
    https://leetcode.com/problems/bulls-and-cows/

    Tags: Google; Medium; HashMap
"""

import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        cows = bulls = 0

        for i in range(len(secret)):
            bulls += secret[i] == guess[i]

        sd = collections.Counter(secret)

        for ch in guess:
            if sd[ch]:
                sd[ch] -= 1
                cows += 1

        cows -= bulls

        return f"{bulls}A{cows}B"
