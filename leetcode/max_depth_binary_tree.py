"""
    https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Tags: POTD; Recursion/BackTracking; Binary Tree; Easy
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Return current height
        if root is None:
            return 0

        # The height at current level will be 1 + max height of children
        depth_left = self.maxDepth(root.left) + 1
        depth_right = self.maxDepth(root.right) + 1

        # Use the max height from any child.
        return max([depth_left, depth_right])
