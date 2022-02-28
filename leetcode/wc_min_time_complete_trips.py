"""
    https://leetcode.com/problems/minimum-time-to-complete-trips/

    Tags: Weekly-Contest_282; Binary Search; Medium
"""

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        # Algo:
        # There exists a value of time 't' for which total Trips can be completed
        # For Any value of time > 't', the trips can be completed too
        # However, for any value < 't' the trips cannot be completed.

        # The trips taken by each bus: 't' / bus_time in time[]

        lo, hi = 1, 10 ** 15

        while lo != hi:
            mid = (lo + hi) // 2

            s = sum(mid // t for t in time)

            print(lo, mid, hi, s)

            if s >= totalTrips:
                hi = mid

            else:
                lo = mid + 1

        return hi
