"""
    https://leetcode.com/problems/logger-rate-limiter/

    Tags: Google; Medium; Stack
"""

from typing import List
from operator import add, sub, mul, floordiv


def div(op1: int, op2: int) -> int:
    neg = (op1 < 0 < op2) or (op2 < 0 < op1)

    ans = floordiv(abs(op1), abs(op2))

    return ans * (-1 if neg else 1)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = {'+': add, '-': sub, '*': mul, '/': div}

        for ch in tokens:
            if ch in ops:
                op2 = stack.pop()
                op1 = stack.pop()

                stack.append(ops[ch](op1, op2))
            else:
                stack.append(int(ch))

            # print(f"{stack} {ch}")

        return stack[0]
