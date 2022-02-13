"""
    https://leetcode.com/problems/01-matrix/

    Tags: Practice; Concepts; Algorithms; BFS/DFS; Medium
"""

from typing import List, Set, Tuple


class Solution:
    def __init__(self):
        # To store nodes which we have visited and whose neighbors we know
        self.visited = set()

        # To store nodes which we have visited and whose neighbors we DON'T know
        self.visiting = set()

        # To store unvisited neighbors
        self.to_visit = set()

        self.dist = 0

    def get_unvisited_neighbors(self, mat: List[List[int]], row: int, col: int) -> Set[Tuple[int, int]]:
        neighbors = set()

        if row - 1 >= 0 and (row - 1, col) not in self.visited:
            neighbors.add((row - 1, col))
        if row + 1 < len(mat) and (row + 1, col) not in self.visited:
            neighbors.add((row + 1, col))
        if col - 1 >= 0 and (row, col - 1) not in self.visited:
            neighbors.add((row, col - 1))
        if col + 1 < len(mat[0]) and (row, col + 1) not in self.visited:
            neighbors.add((row, col + 1))

        return neighbors

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # '0's are already visited
        for i, row in enumerate(mat):
            for j, elem in enumerate(row):
                if elem == 0:
                    self.visited.add((i, j))

        # Update all unvisited neighbors of '0's, i.e. all '1's
        for node in self.visited:
            self.visiting.update(self.get_unvisited_neighbors(mat, node[0], node[1]))

        # Since '1's are already at distance 1, the next distance shall start at '2'
        self.dist = 2

        # Do BFS and in-place update the reachability distance for each new discovered node
        while len(self.visited) < len(mat) * len(mat[0]):

            # We will figure out neighbors of 'visiting' state nodes now, so move them to 'visited'
            self.visited.update(self.visiting)

            # Figure out neighbors of 'visiting' state nodes
            for node in self.visiting:
                self.to_visit.update(self.get_unvisited_neighbors(mat, node[0], node[1]))

            # These nodes are +1 distance away from the last visited nodes
            for node in self.to_visit:
                mat[node[0]][node[1]] = self.dist

            self.dist += 1

            # Setup to figure out next neighbors of current level/distance nodes
            self.visiting = self.to_visit
            self.to_visit = set()

        return mat