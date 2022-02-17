"""
    https://leetcode.com/problems/climbing-stairs/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""


class Solution:
    def __init__(self):
        # For Memoization
        self.dp_ways = {}

    def climbStairs(self, n: int) -> int:

        return self.ways_nth_stair(n)

    def ways_nth_stair(self, n: int):

        if n in {1, 2}:
            return n

        # Ways to reach `i`th stair =
        # Number of Ways to reach `i - 1`th stair + Ways to reach `i - 2`th stair
        if n not in self.dp_ways:
            self.dp_ways[n] = self.ways_nth_stair(n - 1) + self.ways_nth_stair(n - 2)

        return self.dp_ways[n]

