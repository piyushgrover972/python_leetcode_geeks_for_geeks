"""
    https://leetcode.com/problems/sort-list/

    Tags: POTD; Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        trav = head
        vals = []
        while trav:
            vals.append(trav.val)
            trav = trav.next

        vals.sort()

        trav = head
        ival = iter(vals)
        while trav:
            trav.val = next(ival)
            trav = trav.next

        return head
