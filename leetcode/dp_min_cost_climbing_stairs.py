"""
    https://leetcode.com/problems/min-cost-climbing-stairs/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Easy
"""

from typing import List


class Solution:
    def __init__(self):
        self.dp_totalcost = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # The 'top' is 1 beyond the last element.
        return self.dp_cost(len(cost), cost)

    def dp_cost(self, nth: int, cost: List[int]):

        if nth in {0, 1}:
            return 0

        if nth not in self.dp_totalcost:
            # DP Recurrence Relation
            # To reach stair 'i', the total cost would either be
            # `dp_totalcost[i - 1] + cost[i - 1]` or
            # `dp_totalcost[i - 2] + cost[i - 2]`
            # So, we shud take min of either.
            # Therefore, `dp(i) = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            # Base Case:
            # Two Stairs: dp(0) = dp(1) = 0, Since we can start at either index 0 or 1

            cost_1 = self.dp_cost(nth - 1, cost) + cost[nth - 1]
            cost_2 = self.dp_cost(nth - 2, cost) + cost[nth - 2]

            self.dp_totalcost[nth] = min(cost_1, cost_2)

        return self.dp_totalcost[nth]
