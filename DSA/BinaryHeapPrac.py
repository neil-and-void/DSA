class BinaryHeap:
    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[0]

    def insert(self, val):
        '''
        append to end

        # bubble up
        current = len(self.data) - 1
        parent = (current - 1) // 2

        while parent >= 0:
            # check and swap
            if self.data[parent] > self.data[current]:
                # swap
                temp = self.data[parent]
                self.data[parent] = self.data[current]
                self.data[current] = self.data[parent]

            else:
                return
        '''
        self.data.append(val)
        current = len(self.data) - 1
        parent = (current - 1) // 2

        while parent >= 0:
            # check and swap
            if self.data[parent] > self.data[current]:
                # swap
                temp = self.data[parent]
                self.data[parent] = self.data[current]
                self.data[current] = temp

                current = parent
                parent = (current - 1) // 2

            # no swap occurred, in correct spot now
            else:
                return

    def pop(self):
        '''
        swap first with end
        pop end into variable to return later

        current = top element

        while current is not a leaf node
            maxElement = current

            if left exists and is bigger
                left is the new maxelement

            if right exists and is bigger
                right is the new maxelemet

            if maxElement == current (ie no swap occured)
                return popped

            else
                swap maxelement and current values
                current = maxElement
        '''
        n = len(self.data)

        temp = self.data[0]
        self.data[0] = self.data[n - 1]
        self.data[n-1] = temp

        popped = self.data.pop()

        n = len(self.data)
        current = 0
        left = 1
        right = 2

        while left < n or right < n:
            minElement = current

            if left < n and self.data[minElement] > self.data[left]:
                minElement = left

            if right < n and self.data[minElement] > self.data[right]:
                minElement = right

            if minElement == current:
                break

            temp = self.data[minElement]
            self.data[minElement] = self.data[current]
            self.data[current] = temp
            current = minElement
            left = (2 * current) + 1
            right = (2 * current) + 2
        return popped

binaryHeap = BinaryHeap()
from random import randint
for i in range(20):
    binaryHeap.insert(randint(0, 50))

prev = binaryHeap.pop()
while len(binaryHeap.data):
    cur = binaryHeap.pop()
    print(cur)
    print(prev <= cur)
    prev = cur


