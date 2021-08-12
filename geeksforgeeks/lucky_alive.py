"""
    Original Problem: https://practice.geeksforgeeks.org/problems/lucky-alive-person-in-a-circle1229/1
"""

# User function Template for python3
import math


class Solution:
    def find(self, N = 5):
        l = list(range(1, N + 1))
        sword = 0

        while len(l) > 1:
            sword = (sword + 1) % len(l)
            try:
                l.pop(sword)
            except IndexError:
                pass
        return l[0]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    print(ob.find(2000))
    # t = int(input())
    # for _ in range(t):
    #     N = int(input())
    #     ob = Solution()
    #     print(ob.find(N))
# } Driver Code Ends