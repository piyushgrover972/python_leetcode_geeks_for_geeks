"""
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Tags: Concepts; Algorithms; Sliding-Window; Medium
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) in {0, 1}:
            return len(s)

        old = new = 0

        hmap = {s[old]: 0}
        maxsz = 0

        # print(hmap)
        for i, ch in enumerate(s[1:]):
            if ch in hmap:
                new = hmap[ch] + 1

                for j in range(old, new):
                    del hmap[s[j]]

                old = new

            hmap[ch] = i + 1

            maxsz = len(hmap) if len(hmap) > maxsz else maxsz
            # print(hmap)

        return maxsz