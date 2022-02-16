"""
    https://leetcode.com/problems/swap-nodes-in-pairs/

    Tags: POTD; Concepts; Algorithms; Recursion; Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there is no node or single node left, return it as is
        if not head or not head.next:
            return head

        # Save the remaining tail after 2 nodes
        tail = head.next.next

        # Save the 2nd node out of the two nodes.
        child = head.next

        # The 2nd node should point to first node
        head.next.next = head

        # The first node now points to the modified tail
        head.next = self.swapPairs(tail)

        # Return the prev 2nd node, i.e. current first node
        return child
