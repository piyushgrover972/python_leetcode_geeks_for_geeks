"""
    Original Problem: https://practice.geeksforgeeks.org/problems/lucky-alive-person-in-a-circle1229/1
"""


# User function Template for python3
class Solution:
    def find(self, N = 5):
        l = list(range(1, N + 1))
        sword = 0
        killed = None

        while len(l) > 1:
            # The person next to the one having sword is killed (in a circle)...
            killed = (sword + 1) % len(l)
            try:
                # After the person is killed, it is removed from the queue...
                l.pop(killed)
            except IndexError:
                pass

            # Since the killed person is removed, the next person in queue takes its position...
            sword = killed

        return l[0]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    print(ob.find(90))
    # t = int(input())
    # for _ in range(t):
    #     N = int(input())
    #     ob = Solution()
    #     print(ob.find(N))
# } Driver Code Ends