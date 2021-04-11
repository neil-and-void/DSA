import typing

'''
def rotateList(head, k) -> Node:
    count = 0
    while current is not none
        increment coutn

    shiftAmnt = n mod k
    if shiftAmnt == 0:
        return head

    m = n - shiftAmount

    leftSliceHead = head
    current = head
    iterate current m times
    detach current from next
    next becomes the new list head
    go to the end of the rest of the list (until None is found) and reattache leftSliceHead
'''

def rotateList(head):
    n = 0
    current = head
    while current != None:
        n += 1
        current = current.next

    shiftAmount = k % n
    if shiftAmount == 0:
        return head

    m = n - shiftAmount

    leftSliceHead = head
    current = head
    while m:
        m -= 1
        current = current.next
    head = current.next
    current.next = None
    current = head

    while current.next != None:
        current = current.next
    current.next = leftSliceHead

    return head


rotateList()

