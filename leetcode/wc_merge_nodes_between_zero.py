"""
    https://leetcode.com/contest/weekly-contest-281/problems/merge-nodes-in-between-zeros/

    Tags: Weekly-Contest_281; LinkedList; Medium
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Since first node shall always be '0'
        head = head.next

        trav = head

        # Traverse the List
        while trav and trav.next:
            # If next node is '0' node
            if trav.next.val == 0:

                # Remove the '0' node
                trav.next = trav.next.next

                # Set the 'trav' to the node next to '0' node, since there are no two consecutive '0' nodes
                trav = trav.next

            else:

                # Next node is non-'0', add its value to current node's value
                trav.val += trav.next.val

                # Remove the node, i.e. point the current's next to next's next.
                trav.next = trav.next.next

        return head
