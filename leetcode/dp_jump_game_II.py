"""
    https://leetcode.com/problems/jump-game-ii/

    Tags: Practice; Concepts; Algorithms; Dynamic Programming; Medium
"""

from typing import List


# Some constant out of limit of problem constraints
MAX = 2000


class Solution:
    def jump(self, nums: List[int]) -> int:

        # Min Steps to reach last idx from idx 'j' = Min steps to reach from idx 'j + 1' + 1
        #

        target_idx = len(nums) - 1
        start_idx = 0

        dp_cache = {target_idx: 0}

        def dp_min_steps_from(j: int) -> int:

            nonlocal target_idx, dp_cache

            # print(f"from={j} ({j + nums[j]}) to={target_idx} {dp_cache=} ")
            # Base case
            if j == target_idx:
                return 0

            elif nums[j] == 0:
                return MAX

            elif j not in dp_cache:
                if j + nums[j] >= target_idx:
                    dp_cache[j] = dp_cache[target_idx] + 1

                else:
                    steps = set()
                    for i in range(nums[j], 0, -1):
                        if i + j <= len(nums) - 1:
                            steps.add(dp_min_steps_from(j + i) + 1)
                        # print(f"{j}: {steps}")

                    dp_cache[j] = min(steps)

            return dp_cache[j]

        return dp_min_steps_from(start_idx)
