"""
    Original Problem: https://practice.geeksforgeeks.org/problems/number-of-palindromic-strings2706/1
"""

#User function Template for python3
from math import ceil


class Solution:
    def palindromicStrings(self, max_len, max_chars):
        n_str = 0
        mod = (10**9) + 7
        for i in range(1, max_len + 1):
            # Single character strings, viz. "a", "b", etc. and,
            # Repeated single character strings, viz. "aa", "bb", etc.
            if i == 1 or i == 2:
                n_str += max_chars

            elif max_len <= 2 * max_chars:
                combis = 1
                for j in range(int(ceil(i / 2))):
                    combis *= max_chars - j
                n_str += combis
            else:
                # No combinations possible with given constraints
                pass

        return n_str % mod


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,k = input().split()
        n,k = int(n), int(k)

        ob = Solution()
        answer = ob.palindromicStrings(n,k)
        print(answer)

# } Driver Code Ends
