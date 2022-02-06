"""
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

    Tags: Concepts; Algorithms; Two Pointers; Medium; POTD
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        MAX_NUM_COUNT = 2

        cur_num = nums[0]   # len(nums) > 0
        cur_num_count = 1

        cur_idx = 0

        iterr = 1
        count = 0


        while True:
            if iterr < len(nums) and nums[iterr] == cur_num:
                if cur_num_count < MAX_NUM_COUNT:
                    cur_num_count += 1

            else:
                while cur_num_count:
                    nums[cur_idx] = cur_num
                    cur_idx += 1
                    cur_num_count -= 1
                    count += 1

                if iterr < len(nums):
                    cur_num = nums[iterr]
                    cur_num_count = 1
                else:
                    break

            iterr += 1

        return count
