''''''
from typing import *
def diameterOfBinaryTree(root) -> int:
    d = [-1]

    return rec(root, d)

def rec(root, diameter):
    if root == None:
        return 0

    else:
        leftHeight = rec(node.left, diameter)
        rightHeight = rec(node.right, diameter)

        if leftHeight != 0:
            leftHeight += 1
        if rightHeight != 0:
            rightHeight += 1

        diameter[0] = max(leftHeight + rightHeight, diameter[0])
        return max(leftHeight, rightHeight)

