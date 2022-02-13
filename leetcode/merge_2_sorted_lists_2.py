"""
    https://leetcode.com/problems/merge-two-sorted-lists/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Easy

    NOTE: This is the Recursive solution
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # To better understand this algo, dry-run through an example
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        # If one list is None, return the other list
        if not head1:
            return head2
        if not head2:
            return head1

        # The lower value shall be the parent of the list created after merging the two sublists
        if head1.val <= head2.val:
            head1.next = self.mergeTwoLists(head1.next, head2)
            return head1

        else:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2

