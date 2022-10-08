class Node():
    def __init__(self, data):
        self.next = None
        self.data = data

class Var():
    def __init__(self):
        self.head = None
        self.lenght = 0
    
    def add(self, node):
        if self.lenght == 0:
            self.lenght += 1
            self.head = node
        else:
            self.lenght += 1
            n = self.head
            while n.next != None:
                n = n.next
            n.next = node
    
    def show(self):
        node = self.head
        while True:
            print(node.data, end=" ")
            if node.next == None:
                break
            else:
                node = node.next
        print("")
    
    def remove_last(self):
        self.lenght -= 1
        node = self.head
        prev = None
        while True:
            if node.next == None:
                prev.next = None
                break
            else:
                prev = node
                node = node.next
    
    def remove_first(self):
        self.lenght -= 1
        self.head = self.head.next

myvar = Var()
myvar.add(Node(6))
myvar.add(Node(8))
myvar.add(Node(1))
myvar.show()
myvar.remove_last()
myvar.show()