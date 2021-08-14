"""
    Original Problem: https://practice.geeksforgeeks.org/problems/subset-sums2234/1
"""


# User function Template for python3
from itertools import combinations


class Solution:
    def subsetSums(self, arr, N):
        sums = []
        for i in range(N + 1):
            combis = combinations(arr, i)
            sums.extend([sum(t) for t in combis])

        sums = sorted(sums)
        return sums


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends