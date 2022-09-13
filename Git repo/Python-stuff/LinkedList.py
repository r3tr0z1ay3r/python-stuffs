
class node:
    def __init__(self,data):
        self.data = data
        self.address = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        n = node(data)
        temp = self.head
        n.address = temp
        self.head = n
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.address

n1 = node(10)
s1 = SingleLinkedList()
s1.head = n1
s1.insert_begin(20)
s1.display()
