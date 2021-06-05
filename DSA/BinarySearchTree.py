class BinaryNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        '''
        '''
        if self.root == None:
            self.root = BinaryNode(val)
        else:
            self.root = self._insert(val, self.root)

    def _insert(self, val, node):
        '''
        # base
        if current Node is None
            return none
        # Recursive
        if val <, go left
        if val >, go right
        if val ==, return current node and don't insert (or go left depending on what we want to do)
        '''
        # base
        if node == None:
            return BinaryNode(val)

        # recursive
        if val == node.val:
            return node

        if val < node.val:
            # go left
            node.left = self._insert(val, node.left)

        if node.val < val:
            # go right
            node.right = self._insert(val, node.right)
        return node

    def get(self, key):
        '''simpel binary searc'''
        return

    def _get(self, key, node):
        return

    def delete(self, key):
        '''
        recurse like binary search
        when get to element, children are the children of the parent of current node
        '''
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        '''
        # base case
        # if node is None
            return None

        # found the node with key
            # deleting leaf node
            if leaf node
                Return None

            # deleting 1 child node
            if 1 child node
                if left child exists
                    get right most of left node
                if right child exists
                    get left most of right node
                put the val of that node in the current node
                delete that node
                return current

            # deleting 2 child node
            if 2 child nodes
                get right most node of left child
                copy that value to current node
                delete max of left child

        # recursive
        # left side
        if key < node.key
            go left

        # right side
            go right
        '''
        if node == None:
            return None

        if node.val == key:
            # 3 base cases
            # leaf
            if node.left == None and node.right == None:
                return None

            # 2 children
            if (node.left != None and node.right != None) or (node.left != None and node.right == None):
                maxSubtreeNode = self._getMaxOfSubtree(node.left)
                node.left = self._delete(maxSubtreeNode, maxSubtreeNode.val)
                node.val = maxSubtreeNode.val

            # 1 children
            elif node.left == None and node.right == None:
                minSubtreeNode = self._getMinOfSubtree(node.right)
                node.right = self._delete(minSubtreeNode, minSubtreeNode.val)
                node.val = minSubtreeNode.val

        elif key < node.val:
            node.left = self._delete(node.left, key)

        elif node.val < key:
            node.right = self._delete(node.right, key)

        return node


    def _getMinOfSubtree(self, node):
        if node == None:
            return None
        cur = node
        while cur.left != None:
            cur = cur.left
        return cur

    def _getMaxOfSubtree(self, node):
        if node == None:
            return None
        cur = node
        while cur.right != None:
            cur = cur.right
        return cur

    def print(self):
        self._inOrderPrint(self.root)

    def _inOrderPrint(self, node):
        if node:
            self._inOrderPrint(node.left)
            print(node.val)
            self._inOrderPrint(node.right)

bst = BinarySearchTree()

bst.insert(50)
bst.insert(100)
bst.insert(150)

bst.insert(25)
bst.insert(75)

bst.insert(125)

bst.print()

