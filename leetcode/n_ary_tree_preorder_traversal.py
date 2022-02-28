"""
    https://leetcode.com/problems/n-ary-tree-preorder-traversal/

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        l = []
        if root is not None:

            l = [root.val]

            for c in root.children:
                l.extend(self.preorder(c))

        return l
