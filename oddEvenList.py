'''
idea:
'''
def oddEvenList(head):
    # get count and ref to last node
    count = 1
    last = head
    while last.next != None:
        count += 1
        last = last.next

    if count <= 2:
        return head

    # do first swap
    evenPartitionHead = head.next
    cur = head
   
    removed = cur.next
    cur.next = cur.next.next
    removed.next = None
    last.next = removed
    last = last.next

    # continue on with rest of the swaps
    while cur != evenPartitionHead and cur.next != evenPartitionHead:
        removed = cur.next
        cur.next = cur.next.next
        removed.next = None
        last.next = removed
        last = last.next
    return head
