class QNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        if self.head == None and self.tail == None:
            newNode = QNode(val)
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = QNode(val)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head == self.tail:
            dequeued = self.head
            self.head = None
            self.tail = None
            return dequeued.val
        else:
            dequeued = self.head
            self.head = self.head.next
            return dequeued.val

    def print(self):
        cur = self.head

        while cur != None:
            print(cur.val)
            cur = cur.next

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)


q.print()

print('##')
print(q.dequeue())
print('##')

q.print()
