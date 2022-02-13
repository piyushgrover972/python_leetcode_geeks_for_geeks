"""
    https://leetcode.com/problems/merge-two-sorted-lists/

    Tags: Practice; Concepts; Algorithms; Recursion/BackTracking; Easy
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

        # If one list is None, return the other list
        if not head1:
            return head2
        if not head2:
            return head1

        # Our algo assumes head2 will always be at the front of merged list,
        # hence if first node of list2 is greater, swap the heads...
        if head2.val > head1.val:
            head1, head2 = head2, head1

        head = head2

        # We need `head2` to point its `next` to remaining `head1` if it remains after all iterations,
        # hence iterate till `head2->next`
        # On other hand, `head1` can iterate to `None` as it means `head2` list is remaining.
        # Since, all the nodes in `list2` are already sorted, we do not need to do anything further
        while head1 and head2.next:

            # Find the correct place for list1 node
            if head2.val <= head1.val < head2.next.val:

                # Setup the pointers to insert the list1 node between list2 nodes
                tmp1 = head2.next
                tmp2 = head1.next
                head2.next = head1
                head1.next = tmp1
                head1 = tmp2

            head2 = head2.next

        # If list 1 remains, append it at the end of list 2
        if head1:
            head2.next = head1

        return head

