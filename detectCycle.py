'''
idea: floyds cycle detection
def detectCycle(head):
    create a fast and slow pointer
    move pointers until one of them hits None or they collide
    if they collide
        move 1 pointer to the beginning and move both by 1 until collide
        return that node
'''


def detectCycle(head):
    fast = head.next
    slow = head.next.next

    while fast.next != None and fast != slow:
        slow = slow.next
        fast = fast.next.next

    if fast.next == None:
        return 'no cycle'

    if fast == slow:
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow


head = None
res = detectCycle(head)

