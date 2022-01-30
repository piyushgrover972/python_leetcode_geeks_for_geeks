"""
    Original Problem: https://practice.geeksforgeeks.org/problems/cousins-of-a-given-node/1

"""


"""
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""


class Solution:

    def __init__(self):
        self.nodelvl = 0
        self.inc = 1
        self.level = 0
        self.cousins = []

    # Pre-Order Traversal to find the node Level (Level 0 => Root)
    def findLevel(self, node, node_to_find):
        if not node:
            return

        if node.data == node_to_find.data:
            self.inc = 0

        self.nodelvl += self.inc
        self.findLevel(node.left, node_to_find)
        self.findLevel(node.right, node_to_find)
        self.nodelvl -= self.inc

    def printCousins(self, root, node_to_find):
        self.findLevel(root, node_to_find)
        # print(self.nodelvl)
        self.findCousins(root, node_to_find.data)
        return self.cousins if self.cousins else [-1]

    def findCousins(self, node, findval):
        if not node:
            return

        self.level += 1
        self.findCousins(node.left, findval)

        if self.nodelvl > 0 and self.level == self.nodelvl:
            if (not node.left or (node.left.data != findval)) and \
                    (not node.right or (node.right.data != findval)):
                if node.left:
                    self.cousins.append(node.left.data)
                if node.right:
                    self.cousins.append(node.right.data)

        self.findCousins(node.right, findval)
        self.level -= 1


# {
#  Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3

from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree   
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input 
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def pointer(root, n):
    if root == None:
        return None

    if root.data == n:
        return root

    l = pointer(root.left, n)
    if l != None and l.data == n:
        return l

    r = pointer(root.right, n)
    return r


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        s = input()
        root = buildTree(s)
        p = pointer(root, n)
        ob = Solution()
        ans = ob.printCousins(root, p)

        for i in range(len(ans)):
            print(ans[i], end=" ")

        print()

# } Driver Code Ends