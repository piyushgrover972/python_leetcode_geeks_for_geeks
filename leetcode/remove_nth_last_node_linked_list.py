"""
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Tags: Concepts; Algorithms; Two Pointers; Medium/Easy;
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = follower = head

        while n:
            leader = leader.next
            n -= 1

        while leader and leader.next:
            leader = leader.next
            follower = follower.next

        if leader == None:
            head = follower.next

        else:
            follower.next = follower.next.next

        return head

