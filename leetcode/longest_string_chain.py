"""
    https://leetcode.com/problems/longest-string-chain/

    Tags: Google; Medium; Dynamic Programming; String
"""

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if len(words) == 1:
            return 1

        words_set = set(words)

        print(words)
        dp_chain_len = {}

        def dp_find_pred(word: str):

            nonlocal dp_chain_len, words_set

            if word in words_set:

                if word not in dp_chain_len:

                    chain_lens = []

                    for i in range(len(word)):
                        chain_lens.append(dp_find_pred(word[:i] + word[i + 1:]))

                    dp_chain_len[word] = 1 + max(chain_lens)

                return dp_chain_len[word]

            else:

                return 0

        for word in words:
            dp_find_pred(word)

        # print(dp_chain_len)

        return max(dp_chain_len.values())
