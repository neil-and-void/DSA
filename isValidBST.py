'''
idea: check left sub

not good, o(height^2), o(n)
'''
from typing import *
def isValidBST(root: TreeNode) -> bool:
    # base
    if root == None:
        return True

    # recursive
    else:
        leftSubtree = isValidBST(root.left)
        rightSubtree = isValidBST(root.right)

        leftConnection = False
        rightConnection = False
        if root.left == None or (root.left != None and root.left.val < root.val):
            leftConnection = True 
        if root.right == None or (root.right != None and root.val < root.right.val):
            rightConnection = True

        return leftConnection and rightConnection and leftSubtree and rightSubtree

inOrderCopy(root, arr):
    if root:
        inOrderCopy(root.left, arr)
        arr.append(root.val)
        inOrderCopy(root.right, arr)

'''
idea: inorder copy and keep track of the previous smallest of left subtree
'''
prev = float('-inf')
def inorder(root):
    if root == None:
        return True

    else:
        leftSubtree = inorder(root.left)
        if !leftSubtree:
            return False

        valid = False
        if prev < root.val:
            valid = True

        rightSubtree = inorder(root.right)
        if !rightSubtree:
            return False
        
        return True


