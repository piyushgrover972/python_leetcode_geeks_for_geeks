"""
    https://leetcode.com/problems/majority-element/

    Tags: POTD; Boyer-Moore Voting Algo; Easy
"""

import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
