'''
idea: recursion and remove on collapase of the recursion

def removeNthFromEnd(head, n):
    def rec(head, n):
        # base
        if head equals none
            return head, 0

        # recursive
        else:
            nextHead, current_n = rec(head.next, n)
            current_n += 1
            if current_n == n
                # get rid of current node
                
                # if next is not None
                if nextHead is not None
                    head.val = headNext.val
                    head.next = headNext.next
                else if headNext is None
                    head = None

            else:
                head.next = nextHead

            return head, current_n

'''
'''
def removeNthFromEnd(head, n):
    def rec(head, n):
        # base
        if head == None:
            return head, 0

        # recursive
        else:
            nextHead, next_n = rec(head.next, n)
            current_n = next_n + 1

            if current_n == n:
                if nextHead != None:
                    head.val = nextHead.val
                    head.next = nextHead.next

                elif nextHead == None:
                    head = None

            else:
                head.next = nextHead
            
            return current_n 
    head = rec(head, n)
    return head
'''

'''
another idea: offset 2 pointers by n and travel down the list until we have found the end

def removeNthFromEnd(head, n):
    p1 = head
    p2 = head
    
    progress p2 by n

    progress both until p2.next is None
    remove node at p1

    return head
'''

def removeNthFromEnd(head, n):
    pass


