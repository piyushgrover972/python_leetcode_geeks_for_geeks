"""
    https://leetcode.com/problems/permutation-in-string/

    Tags: Concepts; Algorithms; Sliding-Window; Medium
"""
from typing import Dict


class Solution:

    def match_char_counts(self, pattern_chars_count: Dict[int, int], string_chars_count: Dict[int, int]) -> bool:
        for i in range(ord('a'), ord('z') + 1):
            if i in pattern_chars_count:
                if i in string_chars_count and pattern_chars_count[i] == string_chars_count[i]:
                    continue
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        patt_char_cnt = {}
        str_char_cnt = {}

        for ch in s1:
            patt_char_cnt[ord(ch)] = patt_char_cnt.get(ord(ch), 0) + 1

        patlen = len(s1)
        first = 0
        for i in range(len(s2)):
            str_char_cnt[ord(s2[i])] = str_char_cnt.get(ord(s2[i]), 0) + 1

            if i - first == patlen - 1:
                match = self.match_char_counts(patt_char_cnt, str_char_cnt)
                if match:
                    return True

                str_char_cnt[ord(s2[first])] -= 1
                first += 1

        return False
