'''
# idea: go through list and cache nodes and check if we've seen it before
def linkedListCycle(head):
    go through linked list while not reached end
        at each iteration check if node is in set
        if so -> return true
        else add it to set and keep going
    return false at end

# idea: use a slow and fast pointer
def linkedListCycle(head):
    point slowPointer to head
    point fastPointer to head

    move slow and fast pointer along until fast pointer hits end
    or slow pointer is equal to fast pointer

'''

def linkedListCycle(head):
    s = Set()

    current = head
    while current != None:
        if current in s:
            return True
        s.add(current)
        current = current.next
    return False

def linkedListCycleConstantSpace(head):
    slow = head
    fast = head

    while fast != None and fast.next != None and slow != fast:
        fast = fast.next.next
        slow = slow.next

    if slow == fast:
        return True

    else:
        return False

