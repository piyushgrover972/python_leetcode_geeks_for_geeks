"""
    https://leetcode.com/problems/next-greater-element-i

    Tags: Study Plan; Programming Skills; Easy
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Method 2:
        return self.method2(nums1, nums2)

        # Method 1: Naive
        # return self.method1(nums1, nums2)

    def method2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Method 2
        # In one pass over nums2 (the superset),
        # figure out the 'next greater element' (NGE) for each element and save it in a hashmap
        # That will be TC: O(n)
        # Now for each element in nums2, query the hashmap for the next greater
        # That will be TC: O(1)
        # Hence,
        # Total TC: O(n)
        # SC: O(n)

        hmap = {}

        # In this part of code, we try to figure out the NGE of each element in `nums2`
        # Start with last element in `nums2`
        # NOTE: The last element will never have an NGE
        #
        # Take `nxt` idx pointing to the last element (candidate of being an NGE for prev element)
        # Take `cur` idx pointing to the element just previous to `nxt` element.
        #
        # Algo:
        # Case 1: If the `cur` element is less than `nxt` element,
        #         then, the `nxt` element is the NGE for the `cur` element
        #         Save it in the `hmap` as `hmap[nums2[cur]] = nums2[nxt]`
        #
        # Case 2: If the `cur` element is greater than `nxt` element,
        #         then, the NGE for the `nxt` element 'CAN be' the NGE for `cur` element,
        #         if the `nxt`'s NGE is greater than `cur` element
        #         else, keep traversing to the NGE of the `nxt`'s NGE, till we find the appropriate
        #         element greater than `cur`.
        #         If there is no such elemnt, then there is no NGE for `cur`.
        #
        nxt = len(nums2) - 1
        cur = nxt - 1
        while cur >= 0:

            if nums2[cur] < nums2[nxt]:
                hmap[nums2[cur]] = nums2[nxt]

            else:
                nge = nums2[nxt]
                while True:
                    if nge in hmap:
                        nge = hmap[nge]

                        # Found the NGE for `cur` element
                        if nge > nums2[cur]:
                            hmap[nums2[cur]] = nge
                            break
                    # No NGE is there for `cur` element
                    else:
                        break

            nxt -= 1
            cur -= 1

        # Right now, the hmap contains the NGE for (almost) every element
        # If an element is not present in hmap, it means it doesn't have a NGE
        # For example, if the `nums2` is sorted in decreasing order, no element will have a
        # NGE, so hmap would be empty

        ans = [-1] * len(nums1)

        if hmap:
            for i in range(len(nums1)):
                if nums1[i] in hmap:
                    ans[i] = hmap[nums1[i]]

        return ans

    def method1(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Method 1: Naive
        # Let M <= len(nums1); N <= len(nums2)
        # TC: O(NM)
        # SC: O(1)

        ans = [-1] * len(nums1)

        for i, num1 in enumerate(nums1):

            found = False
            for num2 in nums2:

                if found and num2 > num1:
                    ans[i] = num2
                    break

                elif num2 == num1:
                    found = True

        return ans
