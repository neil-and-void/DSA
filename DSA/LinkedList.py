class Node:
    def __init__(self, x):
        self.val = x
        self.next = None



'''
class LinkedList
    def remove(self, item):
        current = self.head
        prev = None

        while current not None and not found:
            if current node val == item:
                found = True
            prev = current
            current = current.next

        # not found
        if found == False:
            return None

        if current == self.head:
            reassign new head to be next of current
        else:
            point prev to next of current
        return removed
'''
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode

    def remove(self, item):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.val == item:
                found = True
            else:
                prev = current
                current = current.next

        if found == False:
            return None

        if current == self.head:
            self.head = current.next
        else:
            prev.next = current.next
        return item

    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

#ll = LinkedList()
#
#ll.add(1)
#ll.add(2)
#ll.add(3)
#ll.add(4)
#ll.add(5)
#
#ll.remove(5)
#
#ll.print()

