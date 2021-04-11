'''
class QNode:
    val
    next
    prev

class Dequeue:
    def init():
        backHead = None
        frontHead = None

    def pushFront(x):
        if dequeue is empty
            x is the new back and front head
        front head points to x
        x is new fronthead

    def pushBack(x):
        if dequeue is empty
            x is the new back and front head
        back head ponts to x
        x is the new head

    def popFront():
        if queue is not empty
            if queue is size 1 (meaning front and back nodes are the same):
                front and back equal to none
                return the front node
            point previous node of front to None
            point prev of front node to none
            return the front node

    def popBack():
        if stack is not empty
            if front and back heads are the same
                both front and back are now none
                return back
            the prev of the next node popints to none
            next of the back node points to none
            return the back node val
'''

class DequeueNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Dequeue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def pushFront(self, x):
        newNode = DequeueNode(x)
        if self.size == 0:
            self.front = newNode
            self.back = newNode
        else:
            self.front.next = newNode
            newNode.prev = self.front
            self.front = newNode
        self.size += 1

    def pushBack(self, x):
        newNode = DequeueNode(x)
        if self.size == 0:
            self.front = newNode
            self.back = newNode
        else:
            self.back.prev = newNode
            newNode.next = self.back
            self.back = newNode
        self.size += 1

    def popFront(self):
        if not self.isEmpty():
            if self.size == 1:
                popped = self.front.val
                self.front = None
                self.back = None
                self.size -= 1
                return popped
            else:
                popped = self.front.val
                self.front.prev.next = None
                newFront = self.front.prev
                self.front.prev = None
                self.front = newFront
                self.size -= 1
                return popped

    def popBack(self):
        if not self.isEmpty():
            self.size -= 1
            if self.size == 1:
                popped = self.back.val
                self.back = None
                self.front = None
                return popped
            else:
                popped = self.back.val
                self.back.next.prev = None
                newBack = self.back.next
                self.back.next = None
                self.back = newBack
                return popped

    def isEmpty(self):
        return not bool(self.size)

    def getSize(self):
        return self.size

    def print(self):
        node = self.back
        while node != None:
            print(node.val)
            node = node.next

def main():
    dq = Dequeue()
    dq.pushBack(9)
    dq.pushFront(8)
    dq.pushBack(10)
    dq.pushFront(5)
    dq.popBack()
    dq.popBack()
    dq.popBack()
    dq.print()


if __name__ == '__main__':
    main()

