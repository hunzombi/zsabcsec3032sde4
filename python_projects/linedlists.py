from logging import RootLogger
import re


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def findLastNode(root):
    current = root
    while current.next:
        current = current.next
    return current

def printLinkedList(root):
    cur = root
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print('\n')
    return 0

def addToList(root, val):
    new_node = Node(val)
    findLastNode(root).next = new_node
    return 0

def getIndex(root, val):
    cur = root
    index = 0
    while cur:
        if cur.val == val:
            return index
        index += 1
        cur = cur.next
    return -1

def getLength(root):
    cur = root
    length = 0
    while cur:
        length += 1
        cur = cur.next
    return length

def removeIndex(root, id):
    cur = root
    index = 0
    while cur:
        if index + 1 == id:
            cont = cur.next.next
            cur.next.next = None
            cur.next = cont
            return 0
        index += 1
        cur = cur.next
    return -1

def reverseList(root):
    nodes = []
    cur = root
    while cur:
        nodes.append(cur)
        cur = cur.next
    nodes = nodes[::-1].append(None)
    lenght = getLength(root)
    for index, node in enumerate(nodes):
        if index < lenght:
            node.next = nodes[index + 1]
    return nodes[0]

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


n = reverseList(a)
print(n.val)
print(n.next.val)
print(n.next.next.val)
print(n.next.next.next.val)
print(n.next.next.next.next.val)
print(n.next.next.next.next.next.val)
printLinkedList(n)