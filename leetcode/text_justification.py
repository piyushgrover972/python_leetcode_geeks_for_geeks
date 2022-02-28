"""
    https://leetcode.com/problems/text-justification/

    Tags: String; Google; Hard
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        start = 0
        width = 0
        spaces = 0
        lines = []

        for i, word in enumerate(words):

            newwidth = width + len(word) + ((i - start) > 0)

            if newwidth <= maxWidth:
                width = newwidth
                spaces = i - start

            else:
                spaces += maxWidth - width

                line = ""

                if i - start > 1:
                    fsp = spaces // (i - start - 1)
                    rsp = spaces % (i - start - 1)

                    for j in range(start, i - 1):
                        line += words[j]
                        line += " " * fsp
                        if rsp:
                            line += " "
                            rsp -= 1

                    line += words[i - 1]

                else:
                    line = words[start] + " " * spaces

                lines.append(line)
                start = i
                width = len(word)
                spaces = 0

        if start < len(words):
            line = ""
            for i in range(start, len(words)):
                line += words[i] + " "

            line = line[:-1]

            line += " " * (maxWidth - len(line))

            lines.append(line)

        return lines

