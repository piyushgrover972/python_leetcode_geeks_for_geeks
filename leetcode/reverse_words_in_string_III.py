"""
    https://leetcode.com/problems/reverse-words-in-a-string-iii/

    Tags: Concepts; Algorithms; Two Pointers, Easy
"""
from typing import List


class Solution:
    def reverseList_inRange(self, sl: List[str], start: int, end_ex: int):
        for i in range((end_ex - start) // 2):
            sl[start + i], sl[end_ex - i - 1] = sl[end_ex - i - 1], sl[start + i]

    def reverseWords(self, s: str) -> str:
        sl = list(s)

        start = 0
        i = 0
        for i, ch in enumerate(sl):
            if ch == ' ':
                self.reverseList_inRange(sl, start, i)
                start = i + 1

        self.reverseList_inRange(sl, start, i + 1)

        return "".join(sl)
