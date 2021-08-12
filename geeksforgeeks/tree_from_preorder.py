"""
    Original Problem: https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1
"""


# User function Template for python3
def constructTree(pre, preLN, n):
    """
    class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
    """
    # code here
    NODE = 'N'
    LEAF = 'L'

    stack = []
    nodes = [Node(val) for val in pre]

    # e.g. [N, N, L, L, L]
    for i, node_type in enumerate(preLN):
        if node_type == NODE:
            stack.append(nodes[i])
            # Since every node will have 0 or 2 children, so 'i + 1' will always
            # be a valid index if node at 'i' is a Node (with 0 child, it will be a Leaf)
            nodes[i].left = nodes[i + 1]
        elif node_type == LEAF:
            try:
                node = stack.pop()
            except IndexError:
                pass
            else:
                node.right = nodes[i + 1]

    return nodes[0]


# {
#  Driver Code Starts
# Initial Template for Python 3
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        pre = list(map(int, input().strip().split()))  # nodes
        preln = list(map(str, input().strip().split()))  # leaf or not
        # construct the tree according to given list
        root = constructTree(pre, preln, n)
        printInorder(root)
        print()
# } Driver Code Ends