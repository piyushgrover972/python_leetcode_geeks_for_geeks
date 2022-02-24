"""
    https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

    Tags: Google; Hard;
"""

from typing import List


# The read4 API is already defined for you.
def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self.fp = 0
        self.buf = []
        self.done = False
        self.fsz = 0

    def read(self, buf: List[str], n: int) -> int:

        # If there is content left in file
        # And the bytes to be read are already read previously
        if not self.done and len(self.buf) < self.fp + n:

            reads = n // 4 + 1

            for i in range(reads):
                tmp = [" "] * 4
                ch = read4(tmp)

                self.buf += tmp[:ch]
                self.fsz += ch

                if ch < 4:
                    self.done = True
                    break

        if self.fp == self.fsz:
            return 0

        else:
            to_read = min(self.fsz - self.fp, n)
            i = 0
            while i < to_read:
                buf[i] = self.buf[self.fp]
                self.fp += 1
                i += 1

        return i
