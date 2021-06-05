'''
idea: inorder traversla ggez
'''

def inorderTraversal(root):
    # base
    if root == None:
        return []

    # 
    else:
        leftArr = inorderTraversal(root.left)
        rightArr = inorderTraversal(root.right)

        return leftArr + root.val rightArr

