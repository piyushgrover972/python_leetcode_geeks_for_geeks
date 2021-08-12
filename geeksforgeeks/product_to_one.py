"""
    Original Problem: https://practice.geeksforgeeks.org/problems/minimum-steps-to-make-product-equal-to-one/1
"""


# User function Template for python3
class Solution:
    def makeProductOne(self, arr, N):
        """
        :algorithm
          Basic Concept:
            a. Find the minimum of the distances of each number from -1 or 1.
            b. Add each distance value.
            c. If the final product comes -1, and if at least one of the element
               in the array was '0', then its fine.
            d. Otherwise, if '0' was not there in the array, add '2' to the total
               difference.
        :param arr: array of integers
        :param N: size of array
        :return: Number of steps required to reduce the product of nums in array to 1.
        """
        diff = 0
        count_neg_1 = 0
        is_zero = False
        for elem in arr:
            to_neg_1 = -1 - elem
            to_pos_1 = 1 - elem
            # print(to_neg_1, abs(to_neg_1), to_pos_1, abs(to_pos_1))
            if abs(to_neg_1) < abs(to_pos_1):
                count_neg_1 += 1
                diff += abs(to_neg_1)
            else:
                diff += abs(to_pos_1)

            if elem == 0 and not is_zero:
                is_zero = True

            # print(count_neg_1, diff)

        if count_neg_1 % 2 == 1 and not is_zero:
            diff += 2

        return diff


# code here

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.makeProductOne(arr, N))
# } Driver Code Ends