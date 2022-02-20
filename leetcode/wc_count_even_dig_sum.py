"""
    https://leetcode.com/contest/weekly-contest-281/problems/count-integers-with-even-digit-sum/

    Tags: Weekly-Contest_281; Brute-Force; Easy
"""


class Solution:
    def countEven(self, num: int) -> int:
        ans = 0

        for i in range(1, num + 1):
            s = str(i)

            # Digit Sum
            sm = sum(map(int, s))
            if sm % 2 == 0:
                ans += 1

        return ans
