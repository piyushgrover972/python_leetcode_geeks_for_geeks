"""
    https://leetcode.com/problems/climbing-stairs/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""


class Solution:
    def __init__(self):
        # For Memoization
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        return self.fibonacci(n)

    def fibonacci(self, n: int) -> int:

        if n == 1 or n == 2:
            return n

        # Save in cache to avoid duplicate recursive call
        elif n not in self.cache:
            self.cache[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        return self.cache[n]
