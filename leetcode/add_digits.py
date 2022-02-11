"""
    https://leetcode.com/problems/add-digits/

    Tags: POTD; Easy;
"""


class Solution:
    def addDigits(self, num: int) -> int:
       if num < 10:
           return num
       summ = num % 9
       return summ if summ else 9
