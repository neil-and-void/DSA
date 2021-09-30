'''
observations:
    * first val in pre is the root
    * first val in inorder is left most
    * last val in pre is right most
    * last val in inorder is right most

def buildTree(preorder, inorder):
    pass
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    i = 0
pre = [3,9,20,15,7]
inord = [9,3,15,20,7]
root = buildTree(pre, inord)

inorderPrint(root)

