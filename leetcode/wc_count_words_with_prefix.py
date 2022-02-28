"""
    https://leetcode.com/contest/weekly-contest-282/problems/counting-words-with-a-given-prefix/

    Tags: Weekly-Contest_282; Brute-Force; Easy
"""

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        f = len(list(filter(lambda a: a.startswith(pref), words)))

        return f
