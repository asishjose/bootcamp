class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        new_node = Node(data)

        if self.head.data == x:
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def delete(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Node not found")
        else:
            n.ref = n.ref.ref


    def display(self):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end = " -> ")
                n = n.ref
            print("None")

ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add_before(25,30)
ll.add_before(5,10)
ll.add_before(1,2)
ll.delete(20)
ll.delete(5)

ll.display()
