class LLNode:
    def __init__(self, data=0, next=None):
        self.next = next
        self.data = data


h3 = LLNode(3)
h = LLNode(1, LLNode(2, h3))

p = h
while p != None:
    print(p.data)
    p = p.next

def rm(head):
    if head.next == None:
        head = None
        return
    head.val = head.next.val
    head.next = head.next.next

rm(h3)

while h != None:
    print(h.data)
    h = h.next


