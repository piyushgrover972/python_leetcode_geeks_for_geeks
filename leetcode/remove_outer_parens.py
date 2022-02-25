"""
    https://leetcode.com/problems/remove-outermost-parentheses/

    Tags: Google Assessment; Stack; Easy
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        stack = []
        prim_deco = []
        j = 0

        # Primary Decomposition
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(ch)

            elif ch == ")":
                stack.pop()

            if not stack:
                prim_deco.append(s[j: i + 1])
                j = i + 1

        print(prim_deco)

        return "".join([d[1:-1] for d in prim_deco])
