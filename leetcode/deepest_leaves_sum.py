"""
    https://leetcode.com/problems/deepest-leaves-sum/

    Tags: Google Assessment; Binary Tree; Medium;
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxht = 0
        self.ht = 0
        self.summ = 0

    def height(self, root: Optional[TreeNode]):

        if root is None:
            return

        self.ht += 1

        if self.maxht < self.ht:
            self.maxht = self.ht

        self.height(root.left)
        self.height(root.right)

        self.ht -= 1

    def dLsum(self, root: Optional[TreeNode]):

        if root is None:
            return

        self.ht += 1

        if self.ht == self.maxht:
            self.summ += root.val

        self.dLsum(root.left)
        self.dLsum(root.right)

        self.ht -= 1

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        self.dLsum(root)

        return self.summ
