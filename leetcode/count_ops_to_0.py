"""
    https://leetcode.com/problems/count-operations-to-obtain-zero/

    Tags: Contest; Algorithms; Easy
"""

class Solution:
    """
    Since subtracting a number from other continuously, essentially
    means dividing the higher one by lower one and taking remainder

    The number of operations shall be the obtained quotient
    """
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2:
            if num1 < num2:
                num1, num2 = num2, num1

            ops += num1 // num2
            num1 = num1 % num2

        return ops
