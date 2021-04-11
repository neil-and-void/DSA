'''
def deleteDuplicates(head):
    observations:
        - sorted
    idea: since the list is sorted, have a slow and fast pointer,
        1 goest to the beingging of contiguous repeated numbers,
        and the other goest to the end
        then reassing the node at the slow pointer to the next of
        the node at the fast opinter (which points to the next node)
    slowPointer = head
    fastPointer = head

    while fast is not none
        distance = 0
        while the values of slow and fast pointes are the same:
            distance += 1
            progress the fast pointer
        if distance == 1
            move previous to node at slow
            move slow pointer to where fast pointer is

        # else the distance between fast and slow is greater than 1
        else:
            if slow points to head:
                reassign head
            else:
                prev.next = fastpointer
            move slow pointer to fast pointer

'''

# delete duplicates 1
def deleteDuplicates(head):
    slowPointer = head
    fastPointer = head

    while fastPointer != None:
        while fastPointer != None and slowPointer.val == fastPointer.val:
            fastPointer = fastPointer.next
        slowPointer.next = fastPointer
        slowPointer = fastPointer

    return head

# delete duplicates 2
def deleteDuplicates(head):
    prev = None
    slowPointer = head
    fastPointer = head

    while fastPointer != None:
        distance = 0
        while fastPointer != None and slowPointer.val == fastPointer.val:
            distance += 1
            fastPointer = fastPointer.next

        if distance == 1:
            prev = slowPointer
            slowPointer = fastPointer

        else:
            if slowPointer == head:
                head = fastPointer
            else:
                prev.next = fastPointer
            slowPointer = fastPointer
    return head

