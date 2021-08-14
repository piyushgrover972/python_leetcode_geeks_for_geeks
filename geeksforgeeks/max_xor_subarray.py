"""
    Original Problem: https://practice.geeksforgeeks.org/problems/a512e4b2e812b6df2159b19cc7090ffc1ab056dd/1
"""

"""Python implementation for a Trie based solution
to find max subArray XOR"""


class Node:
    """structure of Trie Node"""

    def __init__(self, data):
        self.data = data
        self.zero = None  # left node for 0
        self.one = None  # right node for 1


class Trie:
    """ class for implementing Trie """
    def __init__(self):
        self.root = Node(0)

    def insert(self, pre_xor):
        """insert pre_xor to trie with given root"""

        self.temp = self.root

        """start from msb, insert all bits of pre_xor
        into the Trie"""
        for i in range(5, -1, -1):

            """Find current bit in prefix sum"""
            val = pre_xor & (1 << i)

            if val:
                """create new node if needed"""
                if not self.temp.one:
                    self.temp.one = Node(0)
                self.temp = self.temp.one

            if not val:
                """create new node if needed"""
                if not self.temp.zero:
                    self.temp.zero = Node(0)
                self.temp = self.temp.zero

        """store value at leaf node"""
        self.temp.data = pre_xor

    def query(self, xor):
        """find the maximum xor ending with last number
            in prefix XOR and return the XOR of this"""

        self.temp = self.root

        for i in range(5, -1, -1):

            """find the current bit in prefix xor"""
            val = xor & (1 << i)

            """Traverse the trie, first look for opposite bit
                and then look for same bit"""
            if val:
                if self.temp.zero:
                    self.temp = self.temp.zero
                elif self.temp.one:
                    self.temp = self.temp.one
            else:
                if self.temp.one:
                    self.temp = self.temp.one
                elif self.temp.zero:
                    self.temp = self.temp.zero

        return xor ^ self.temp.data

    def maxSubArrayXOR(self, n, Arr):
        """returns maximum XOR value of subarray"""

        """insert 0 in the trie"""
        self.insert(0)

        """initialize result and pre_xor"""
        result = -float('inf')
        pre_xor = 0

        """traverse all input array element"""
        for i in range(n):
            """update current prefix xor and insert it into Trie"""
            pre_xor = pre_xor ^ Arr[i]
            self.insert(pre_xor)

            """Query for current prefix xor in Trie and update result"""
            result = max(result, self.query(pre_xor))

        return result


"""Driver program to test above functions"""
if __name__ == "__main__":
    Arr = [8, 1, 2, 12]
    n = len(Arr)
    trie = Trie()
    print(trie.maxSubArrayXOR(n, Arr))
