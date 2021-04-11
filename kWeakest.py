class MinHeap:
    def __init__(self, data=[]):
        self.data = data

    def _minHeapify(self):
        # takes an almost heap (heap everywhere except for root) and restores heap property
        idx = 0
        while idx < len(self.data):
            # if current > left child
            leftChild = self._lChild(idx)
            rightChild = self._rChild(idx)
            if leftChild < len(self.data) and self.data[idx] > self.data[leftChild]:
                self._swap(idx, leftChild)
                idx = self._lChild(idx)

            # if current > right child
            elif rightChild < len(self.data) and self.data[idx] > self.data[rightChild]:
                self._swap(idx, self._rChild(idx))
                idx = self._rChild(idx)

            else:
                return

    def _swap(self, node1, node2):
        tmp = self.data[node1]
        self.data[node1] = self.data[node2]
        self.data[node2] = tmp

    def _parent(self, idx):
        return idx // 2

    def _lChild(self, idx):
        return (2 * idx) + 1

    def _rChild(self, idx):
        return (2 * idx) + 2

    def insert(self, node):
        self.data.append(node)
        current = len(self.data) - 1
        while current >= 0 and self.data[current] < self.data[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def popMin(self):
        self._swap(0, len(self.data) - 1)
        minNode = self.data.pop()
        self._minHeapify()
        return


class SoldierMinheap:
    def __init__(self):
        self.data = []

    def getIndex(self, node):
        return self.data[node][0]

    def getSoldiers(self, node):
        return self.data[node][1]

    def parent(self, curNode):
        return curNode // 2

    def lChild(self, curNode):
        return (2 * curNode) + 1

    def rChild(self, curNode):
        return (2 * curNode) + 2

    def minHeapify(self):
        # we start from an almost heap (heap everywhere except for root)
        # push down until heap property is restored
        curNode = 0
        while curNode < len(self.data):
            leftChild = self.lChild(curNode)
            rightChild = self.rChild(curNode)

            if leftChild < len(self.data) and (
                    (self.getSoldiers(leftChild) < self.getSoldiers(curNode))
                    or ((self.getIndex(leftChild) < self.getIndex(curNode)) and (self.getSoldiers(curNode) == self.getSoldiers(leftChild)))):
                self.swap(leftChild, curNode)
                curNode = leftChild

            elif rightChild < len(self.data) and (
                    self.getSoldiers(rightChild) < self.getSoldiers(curNode)
                    or ((self.getIndex(rightChild) < self.getIndex(curNode)) and (self.getSoldiers(rightChild) == self.getSoldiers(curNode)))):
                self.swap(leftChild, curNode)
                curNode = rightChild

            else:
                return

    def insert(self, data):
        """
        insert at back and bubble up
        """
        self.data.append(data)
        curNode = len(self.data) - 1
        parent = self.parent(curNode)

        while (curNode >= 0 and
                (self.getSoldiers(curNode) < self.getSoldiers(parent))
                or ((self.getSoldiers(curNode) == self.getSoldiers(parent)) and (self.getIndex(curNode) < self.getIndex(parent)))):
            self.swap(curNode, parent)
            curNode = parent
            parent = self.parent(curNode)

    def swap(self, node1, node2):
        """
        swap values at node1 and node 2
        """
        tmp = self.data[node1]
        self.data[node1] = self.data[node2]
        self.data[node2] = tmp

    def popMin(self):
        self.swap(0, len(self.data) - 1)
        popped = self.data.pop()
        self.minHeapify()
        return popped


soldierMinheap = SoldierMinheap()

soldierMinheap.insert((0, 2))
soldierMinheap.insert((1, 4))
soldierMinheap.insert((2, 1))
soldierMinheap.insert((3, 2))
soldierMinheap.insert((4, 5))

print(soldierMinheap.popMin())
print(soldierMinheap.popMin())
print(soldierMinheap.popMin())
print(soldierMinheap.data)
