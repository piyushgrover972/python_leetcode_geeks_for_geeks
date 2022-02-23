"""
    https://leetcode.com/problems/excel-sheet-column-number/

    Tags: POTD; Easy; Maths
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        offset = ord('A') - 1
        base = 26

        summ = 0

        for ch in columnTitle:
            summ = summ * base + ord(ch) - offset

        return summ
