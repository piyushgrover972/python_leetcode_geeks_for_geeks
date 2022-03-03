"""
    https://leetcode.com/problems/is-subsequence/

    Tags: Dynamic Programming; Easy; POTD
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        i_ss = 0

        for ch in t:
            if ch == s[i_ss]:
                i_ss += 1

            if i_ss == len(s):
                return True

        return False
