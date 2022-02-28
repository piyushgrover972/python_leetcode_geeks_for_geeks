"""
    https://leetcode.com/problems/happy-number/

    Tags: Study Plan; Programming Skills; Easy
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        seen = {n}
        c = 0
        while n != 1:
            c += 1
            n = sum(map(lambda k: k * k, map(int, str(n))))

            if n != 1 and n in seen:
                # print(c)
                return False
            else:
                seen.add(n)

        # print(c)
        return True
