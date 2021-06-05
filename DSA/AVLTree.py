class TreeNode:
    def __init__(self, val):
        self.val = val
        self.height = 0
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        self.root = None

    def put(self, item):
        self.root = self._put(item, self.root)

    def _put(self, item, node):
        '''
        # base
        node is none (ie. found spot to put new item)
            put node here and return

        # recursive
        if node exists
            increase height of current node
            if item < node.val
                keep looking for spot in left ndoe

            else if node.val < item
                keep looking for spot in right node

            if children height differ more than 1
                balance it
                (see rebalance method)
        '''
        # base
        if node == None:
            return TreeNode(item)

        else:
            # recursive 
            if item <= node.val:
                node.left = self._put(item, node.left)
                node.height += 1

            elif node.val < item:
                node.right = self._put(item, node.right)
                node.height += 1

            return node

    def _rebalance(self, node):
        '''
        # rebalances node

        given: since we always rebalance a subtree when balance is out of range [-1, 1]
               and balance can only change by 1, node must have a balance that is -2 or 2

        algorithm
        if left height is bigger:
            # case 1
            if left height is bigger
                rotate right (node)
                pass
        
            # case 3
            elif right height is bigger
                rotate left (node)
                pass

        elif right height is bigger:
            # case 4
            if left height is bigger
                

            # case 2
            elif right height is bigger
                pass
        '''
        pass

    def _leftRotate(self, node):
        '''
        newRoot = right of node
        node.right = newRoot.left
        newRoot.left = node
    
        node.height = max(left, right) + 1
        newRoot.height = max(left, right) + 1
        '''
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node

        leftHeight = 0
        if node.left:
            leftHeight = node.left.height
        rightHeight = 0
        if node.right:
            rightHeight = node.right.height
        node.height = max(leftHeight, rightHeight) + 1


        leftHeight = 0
        if newRoot.left:
            leftHeight = newRoot.left.height
        rightHeight = 0
        if newRoot.right:
            rightHeight = newRoot.right.height
        newRoot.height = max(leftHeight, rightHeight) + 1

        return newRoot 

    def _rightRotate(self, node):
        '''
        newRoot = left of node
        node.left = newRoot.right
        newRoot.right = node

        node.height = max(left, right) + 1
        newRoot.height = max(left, right) + 1
        '''
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        pass

    def _print(self, node):
        if node:
            self._print(node.left)
            print('|' + str(node.val), str(node.height))
            self._print(node.right)

    def print(self):
        self._print(self.root)
        return ''

avl = AVL()

avl.put(30)
avl.put(40)
avl.put(50)

avl.print()

print('###')
avl._print(avl._leftRotate(avl.root))
