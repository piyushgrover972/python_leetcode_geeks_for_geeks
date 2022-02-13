"""
    https://leetcode.com/problems/reverse-linked-list/

    Tags: Practice; Concepts; Algorithms; Recursion/Backtracking; Easy
"""
from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there is 0 or 1 node in list, return as is
        if not head or not head.next:
            return head

        # First call to recursive reverse function
        root, node = self.rvrsList_r(head)
        node.next = None

        return root

    # Recursively call this function on head->next
    # At the base case, return the last node (as new head/root) and
    # the last node as a `parent` whose `next` needs to be modified (for reversal)
    # For other than base case, after 'head recursion' return the root-node to callee and
    # update the `next` of returned node to be current node.
    # At the end, return the `(root, cur_node)` tuple.
    def rvrsList_r(self, curnode: Optional[ListNode]) -> Tuple[Optional[ListNode], Optional[ListNode]]:

        # If this is last node... (this will become first/root)
        if curnode.next is None:
            return curnode, curnode

        # First value of returned tuple is the `root` node to be carried all the way up to the
        # top of recursion stack to make it new `root/head`
        # Second value is the child node, whose `next` needs to be updated to current node (parent),
        # i.e. old_child becomes new_parent and old_parent becomes new_child
        root, new_parent = self.rvrsList_r(curnode.next)
        new_parent.next = curnode

        # Return the `root` and curnode, which will become new_parent of its cur_parent
        return root, curnode

