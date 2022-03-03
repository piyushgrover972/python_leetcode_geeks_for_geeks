"""
    https://leetcode.com/problems/get-maximum-in-generated-array/

    Tags: Algorithms; Dynamic Programming; Easy
"""


class Solution:
    def getMaximumGenerated(self, num: int) -> int:

        dp_cache = {}
        mx = 0

        def dp_max(n: int):

            nonlocal mx, dp_cache

            if n in {0, 1}:
                mx = n
                return n

            if n not in dp_cache:
                dp_cache[n] = dp_max(n // 2)

                if n % 2:
                    dp_cache[n] += dp_max((n // 2) + 1)

            if mx < dp_cache[n]:
                mx = dp_cache[n]

            return dp_cache[n]

        for i in range(num + 1):
            dp_max(i)

        return mx
