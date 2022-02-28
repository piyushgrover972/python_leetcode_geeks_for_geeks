"""
    https://leetcode.com/problems/counting-bits/

    Tags: Dynamic programming; Bit Manipulation; Easy
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        # Whenever a new MSB is added to the number it increases the Count of 1s by 1
        # i.e.
        # 0b0 => 0
        # 0b1 => 1
        # Now,
        # 2 => '0b10' => MSB '1' added to '0b0', So count => 1 + 0 = 1
        # 3 => '0b11' => MSB '1' added to '0b1', So count => 1 + 1 = 2
        # Similary for 3-bit numbers:

        # 4 => '0b100' => MSB '1' added to '0b0', So count => 1 + 0 = 1
        # 5 => '0b101' => MSB '1' added to '0b1', So count => 1 + 1 = 2
        # 6 => '0b110' => MSB '1' added to '0b10', So count => 1 + 1 = 2
        # 7 => '0b111' => MSB '1' added to '0b11', So count => 1 + 2 = 3
        # ...

        if n == 0:
            return [0]

        ans = [0, 1]

        while len(ans) < n + 1:
            ans.extend([b + 1 for b in ans])

        return ans[: n + 1]
