"""
    Original Problem: https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string1956/1
"""

class Solution:
    def is_palin(self, s: str) -> bool:
        l = len(s)
        palin = True
        for i, ch in enumerate(s[:l//2]):
            palin = ch == s[l - 1 - i]
            if not palin:
                break

        return palin

    def longestPalindrome(self, S):
        palins = []
        l = len(S)
        for i in range(l):
            # i = 2
            for j in range(i + 1, l + 1):
                subs = S[i:j]
                if self.is_palin(subs):
                    palins.append(subs)

        print(palins)
        longest = ""
        for p in palins:
            longest = longest if len(longest) >= len(p) else p

        return longest

# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input().strip()
        ob = Solution()
        print(ob.longestPalindrome(S))
# } Driver Code Ends