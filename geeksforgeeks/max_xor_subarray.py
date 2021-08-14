"""
    Original Problem: https://practice.geeksforgeeks.org/problems/a512e4b2e812b6df2159b19cc7090ffc1ab056dd/1
"""
import math

MAX_BITS = int(math.log2(10**2))


class TrieNode:
    def __init__(self, value: str):
        self._data = value
        self._next = []

    @property
    def value(self):
        return self._data

    @property
    def links(self):
        return self._next

    def setnext(self, value):
        node = self.getnext(value)
        if node:
            return node
        else:
            node = self.__class__(value)
            self.links.append(node)
            return node

    def removelink(self, value: str):
        try:
            self.links.remove(self.getnext(value))
        except ValueError:
            pass

    def getnext(self, value: str):
        for i, node in enumerate(self.links):
            if node.value == value:
                return node
        return None


class BitsTrie:
    def __init__(self, arr: list):
        self._trie = TrieNode('root')
        self.create(arr)

    def create(self, arr: list):
        for val in arr:
            binval = bin(val)[2:]
            binval = '0' * (MAX_BITS - len(binval)) + binval
            self.insert(binval)

    def insert(self, val: str):
        nexxt = self._trie
        for bit in val:
            nexxt = nexxt.setnext(bit)

    def display(self):
        self._display_recursive(self._trie, 0)

    def _display_recursive(self, node, level):
        print("{}. {}".format(level, node.value))
        for link in node.links:
            self._display_recursive(link, level + 1)


class Solution:
    def maxSubarrayXOR(self, N, arr):
        pass


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    trie = BitsTrie([9, 13, 12, 17, 25])
    trie.display()
    # t = int(input())
    # for _ in range(t):
    #     N = int(input())
    #     arr = input().split()
    #     for itr in range(N):
    #         arr[itr] = int(arr[itr])
    #
    #     ob = Solution()
    #     print(ob.maxSubarrayXOR(N, arr))

# } Driver Code Ends