"""
    https://leetcode.com/problems/decode-string/

    Tags: Google; Medium; String; Recursion/Stack
"""

from typing import Tuple


digs = "0123456789"
chars = "".join(map(chr, range(ord("a"), ord("z") + 1)))

REPS = 1
STR = 2
IDLE = 3


class Solution:
    def decodeString(self, s: str) -> str:

        return self.decoder(s)[0]

    def decoder(self, inp: str) -> Tuple[str, int]:

        state = IDLE

        ans = ""
        rep = 0
        s = ""

        i = 0

        while i < len(inp):

            ch = inp[i]
            # print(f" {ch} {state} {ans}")

            if state == IDLE:
                if ch in digs:
                    state = REPS
                    rep = int(ch)

                elif ch == "]":
                    return ans, i - 1

                else:
                    ans += ch

            elif state == REPS:
                if ch in digs:
                    rep = rep * 10 + int(ch)

                elif ch == '[':
                    state = STR

            elif state == STR:
                if ch in digs:
                    temp, idx = self.decoder(inp[i:])
                    i += idx
                    s += temp

                elif ch in chars:
                    s += ch

                elif ch == ']':
                    ans += s * rep
                    state = IDLE
                    s = ""

            i += 1

        return ans, 0
