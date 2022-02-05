"""
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Tags: Concepts; Algorithms; Two Pointers; Medium

"""
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0

        start, end = 0, len(numbers) - 1

        while start < end:
            summ = numbers[start] + numbers[end]
            if summ == target:
                return [start + 1, end + 1]
            elif summ < target:
                start += 1
            elif summ > target:
                end -= 1
