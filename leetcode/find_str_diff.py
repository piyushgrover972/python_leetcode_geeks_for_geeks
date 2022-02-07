"""
    https://leetcode.com/problems/find-the-difference/

    Tags: POTD; Easy;
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = 0
        for ch in t:
            sum1 += ord(ch)

        for ch in s:
            sum1 -= ord(ch)

        return chr(sum1)