"""
    https://leetcode.com/problems/rotting-oranges/

    Tags: Practice; Concepts; Algorithms; BFS/DFS; Medium
"""
from typing import List

# Grid Cell Types/Values
ROTTEN = 2
FRESH = 1
EMPTY = 0


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.bfs_rotting(grid)

    def bfs_rotting(self, oranges: List[List[int]]):
        # Queue-1 to store list of rotten oranges at current time
        q1 = []

        # Minutes elapsed
        mins = 0

        # Number of fresh oranges in Grid
        fresh = 0

        # Figure out currently FRESH and ROTTEN oranges
        for i, row in enumerate(oranges):
            for j, orange in enumerate(row):
                if orange == ROTTEN:
                    q1.append((i, j))
                elif orange == FRESH:
                    fresh += 1

        # print(f"<< {q1} >>")

        # BFS...
        # While we are seeing Rotten Oranges...
        while q1:
            # Queue-2 to store list of all oranges who will rot in upcoming minute due to currently
            # rotten oranges (`q1`)
            q2 = []

            # While we have not visited all neighbors of all currently rotten oranges
            while q1:
                row, col = q1.pop(0)

                # Mark all the FRESH neighbor oranges as ROTTEN
                # Up
                if row - 1 >= 0 and oranges[row - 1][col] == FRESH:
                    oranges[row - 1][col] = ROTTEN
                    q2.append((row - 1, col))

                # Down
                if row + 1 < len(oranges) and oranges[row + 1][col] == FRESH:
                    oranges[row + 1][col] = ROTTEN
                    q2.append((row + 1, col))

                # Left
                if col - 1 >= 0 and oranges[row][col - 1] == FRESH:
                    oranges[row][col - 1] = ROTTEN
                    q2.append((row, col - 1))

                # Right
                if col + 1 < len(oranges[0]) and oranges[row][col + 1] == FRESH:
                    oranges[row][col + 1] = ROTTEN
                    q2.append((row, col + 1))

            # Update `fresh` oranges by subtracting oranges which rot in this minute
            fresh -= len(q2)

            # Update the `mins` if at least 1 orange got rotten in this minute.
            mins += bool(len(q2))

            # Setup for next iteration, i.e. for figuring out next set of rotten neighbor oranges
            q1, q2 = q2, []

            # print(f"<< {q1}, {fresh=}, {mins=} >>")

        # If we still have fresh oranges left, it means they were unreachable from all ROTTEN oranges at any time
        return mins if not fresh else -1
