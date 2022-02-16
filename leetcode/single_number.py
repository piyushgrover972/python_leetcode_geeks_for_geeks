"""
    https://leetcode.com/problems/single-number/

    Tags: POTD; Bit Manipulation; Easy
"""

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # For a number 'n', (n xor n) => 0,
        # hence the following will zero out all pairs except the lone number
        return reduce(xor, nums)