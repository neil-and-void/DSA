"""
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        append to end

        while parent exists and current greater than parent:
            swap current and parent
            reassign current to parent

    def pop(self, x):
        swap first and last
        pop last to a varible for later

        biggest = current

        while current has at least 1 child

            if left greater than biggest:
                left is the new biggest

            if right greater than biggest:
                right is the new biggest

            is biggest == current ?
                if yes break
                if no, swap biggest and current
                current = biggest

        return poppped
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)

        curr = len(self.heap) - 1
        parent = (curr - 1) // 2

        while parent >= 0 and self.heap[curr] > self.heap[parent]:
            tmp = self.heap[curr]
            self.heap[curr] = self.heap[parent]
            self.heap[parent] = tmp

            curr = parent
            parent = (curr - 1) // 2


    def pop(self):
        tmp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = tmp

        popped = self.heap.pop()

        current = 0
        biggest = 0
        left = 1
        right = 2

        while left < len(self.heap) or right < len(self.heap):

            if left < len(self.heap) and self.heap[left] > self.heap[current]:
                biggest = left

            if right < len(self.heap) and self.heap[right] > self.heap[biggest]:
                biggest = right

            if biggest == current:
                break
            else:
                 tmp = self.heap[biggest]
                 self.heap[biggest] = self.heap[current]
                 self.heap[current] = tmp

                 current = biggest
                 left = (2 * current) + 1
                 right = (2 * current) + 2

        return popped

