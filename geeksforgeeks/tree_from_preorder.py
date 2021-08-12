"""
    Original Problem: https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1
"""

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""


# User function Template for python3
def constructTree(pre, preLN, n):
    """
    Construct a tree using the preorder traversal and some more info
    :algorithm
        1. The first node is root of tree
        2. Since, every node in the binary tree has either 0 or 2 children, the node next to 'N' type node
           will always be the left child of that node.
        3. Now, for every 'N' node, keep setting its left child as the next node in the sequence. Keep pushing
           the node into a stack as its right child is yet to be determined.
        4. If a 'L' leaf node appears, that means the node next to this Leaf is the right child of the top node
           in the stack.
        5. Pop the top node and set it's right child to the node next to the leaf.
        6. Keep proceeding from step 3
    :param pre: preorder traversal of tree
    :param preLN: Indicates whether a node is 'N' (Node) or 'L' (Leaf)
    :param n: number of nodes
    :return: Root of constructed tree
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