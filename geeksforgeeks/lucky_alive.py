"""
    Original Problem: https://practice.geeksforgeeks.org/problems/lucky-alive-person-in-a-circle1229/1
"""


# User function Template for python3
class Solution:
    def next_alive(self, l: list, pos: int):
        try:
            p = l.index(1, pos + 1)
        except ValueError:
            p = l.index(1, 0)

        return p

    def find(self, N = 5):
        l = [1] * N
        sword = 0
        killed = None

        while True:
            # The person next to the one having sword is killed (in a circle)...
            killed = self.next_alive(l, sword)

            if sword == killed:
                break

            # After the person is killed, it is removed from the queue...
            l[killed] = 0

            # Since the killed person is removed, the next person in queue takes its position...
            sword = self.next_alive(l, killed)

        return sword + 1


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