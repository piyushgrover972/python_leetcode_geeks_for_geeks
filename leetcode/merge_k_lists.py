"""
    https://leetcode.com/problems/merge-k-sorted-lists/

    Tags: POTD; Concepts; Algorithms; Divide_n_Conquer; Hard
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Split the list into half
        # Create a function to merge 2 halfs and call it
        # Create a function for recursion base condition to merge 2 lists.

        mergedList = self.mergeHalfKLists(lists)

        return mergedList

    def mergeHalfKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lenn = len(lists)
        if lenn == 0:
            return None

        if lenn == 1:
            return lists[0]

        if lenn == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        list1 = self.mergeHalfKLists(lists[: lenn // 2])
        list2 = self.mergeHalfKLists(lists[lenn // 2:])

        return self.mergeTwoLists(list1, list2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        idx_l1 = list1
        idx_l2 = list2

        if idx_l1.val > idx_l2.val:
            idx_l1, idx_l2 = idx_l2, idx_l1

        head = idx_l1

        while idx_l1.next and idx_l2:

            if idx_l1.val <= idx_l2.val and idx_l2.val < idx_l1.next.val:
                temp = idx_l1.next
                idx_l1.next = idx_l2
                temp2 = idx_l2.next
                idx_l2.next = temp
                idx_l2 = temp2

            idx_l1 = idx_l1.next

        if idx_l2:
            idx_l1.next = idx_l2

        return head
