class Node(object):
    def __init__(self):
        self.val = None
        self.next = None

def printList(root):
    res = []
    while root:
        res.append(str(root.val))
        root = root.next
    print(' -> '.join(res))

def mergeLists(root1, root2):
    prev1 = root1
    prev2 = root2
    cur1 = root1.next
    cur2 = root2.next

    while cur1 and cur2:
        prev1.next = prev2
        prev2.next = cur1
        prev1 = cur1
        prev2 = cur2
        cur1 = cur1.next
        cur2 = cur2.next
    
    if cur2:
        prev1.next = prev2
    
    if cur1:
        cur = root1
        while cur.next != None:
            cur = cur.next
        if cur != cur1:
            prev2.next = cur
    
    return root1

a = Node()
b = Node()
c = Node()
d = Node()
e = Node()
f = Node()
g = Node()
h = Node()
i = Node()
j = Node()

a.val = "a"
b.val = "b"
c.val = "c"
d.val = "d"
e.val = "e"
f.val = "f"
g.val = "g"
h.val = "h"
i.val = "i"
j.val = "j"

a.next = c
c.next = e
e.next = g
g.next = i

b.next = d
d.next = f
f.next = h
h.next = j

ab = mergeLists(a, b)
print("List merged")
printList(ab)