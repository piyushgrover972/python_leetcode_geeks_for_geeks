"""
    https://leetcode.com/problems/n-th-tribonacci-number/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""


class Solution:
    def __init__(self):

        # DP Cache to 'remember' calculated tribonacci values
        self.dp_trib_cache = {}

    def tribonacci(self, n: int) -> int:

        # Tribonacci Recurrence Base case
        if n in {0, 1, 2}:
            return int(bool(n))

        # Cache Miss: Calculate `tribonacci(n)` and save/cache it
        elif n not in self.dp_trib_cache:
            self.dp_trib_cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        # Return saved value from cache
        return self.dp_trib_cache[n]
