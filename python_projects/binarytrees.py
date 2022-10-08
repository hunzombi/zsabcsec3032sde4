
class Stack():
    def __init__(self):
        self.elements = []
    
    def add(self, val):
        self.elements.append(val)
    
    def pop(self):
        res = self.elements.pop(0)
        return res
    
    def empty(self):
        return len(self.elements) == 0

class Node():
    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def depthFirstValue(root):
    if root == None:
        return []
    
    leftValues = depthFirstValue(root.left)
    rightValues = depthFirstValue(root.right)
    return [root.value] + leftValues + rightValues

def breadthFirstValue(root):
    if root == None:
        return []
    stack = Stack()
    current = root
    result = []
    while True:
        result.append(current.value)
        if current.left:
            stack.add(current.left)
        if current.right:
            stack.add(current.right)
        if stack.empty():
            break
        current = stack.pop()
    return result

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(depthFirstValue(a))
print(breadthFirstValue(a))