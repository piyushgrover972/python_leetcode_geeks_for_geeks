"""
    https://leetcode.com/problems/fibonacci-number/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""


class Solution:
    def __init__(self):
        self.dp_fib_cache = {}

    def fib(self, n: int) -> int:

        # Recurrence base Case
        if n in {0, 1}:
            return n

        # Cache Miss: If this value is not cached yet...
        elif n not in self.dp_fib_cache:
            # Do recursive call to calculate and save it
            self.dp_fib_cache[n] = self.fib(n - 1) + self.fib(n - 2)

        # Finally return the value from cache
        return self.dp_fib_cache[n]
