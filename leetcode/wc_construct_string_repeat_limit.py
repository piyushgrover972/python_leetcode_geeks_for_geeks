"""
    https://leetcode.com/contest/weekly-contest-281/problems/construct-string-with-repeat-limit/

    Tags: Weekly-Contest_281; HashMap; Medium
"""

import collections


class Solution:
    def repeatLimitedString(self, s: str, rl: int) -> str:

        # If there is a single repeating character in the string
        if len(set(s)) == 1:
            return s[:rl]

        # Get counts of each char
        cnts = collections.Counter(s)
        cnts = dict(cnts)

        ans = ""

        # The lexicographically highest char (LHC) in the string
        ch_m = max(cnts)

        # The lexicographically second-highest char (LSHC) in the string
        ch_m2 = max(cnts.keys() - {ch_m})

        while cnts:

            # If the count of LHC, is less than RepeatLimit (RL)
            if cnts[ch_m] <= rl:

                # Use all the available number of that char
                ans += ch_m * cnts[ch_m]

                # Remove that char from the HashMap
                cnts.pop(ch_m)

                # Since LHC is already used, LSHC will be the new LHC
                ch_m = ch_m2

                # Find the next LSHC, if we have further chars available in the hashmap/string
                if len(cnts) > 1:
                    ch_m2 = max(cnts.keys() - {ch_m})

                # No more chars left, only LHC is left: This will be handled outside the loop.
                else:
                    break

            # Else, number of LHC is more than RL
            else:

                # Append RL chars to the string
                ans += ch_m * rl

                # Since RL chars are used out of all available in hashmap/string, subtract the number of used chars
                cnts[ch_m] -= rl

                # Now insert '1' LSHC
                ans += ch_m2

                # Decrease the count of LSHC in the hashmap by 1
                cnts[ch_m2] -= 1

                # If the count of LSHC reduces to '0', recalculate the new LSHC, with same logic as above.
                if cnts[ch_m2] == 0:
                    cnts.pop(ch_m2)
                    if len(cnts) > 1:
                        ch_m2 = max(cnts.keys() - {ch_m})
                    else:
                        break

        # If a character is left in cnts...
        if cnts:
            # Get the char and its count
            ch, v = cnts.popitem()

            # Append the remaining char to the `ans`.
            ans += ch * min(rl, v)

        return ans
