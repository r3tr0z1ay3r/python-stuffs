class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queueSLL:
    def __init__(self):
        self.head = None
    def enqueue(self,data):
        new = node(data)
        if self.head == None:
            n = node(data)
            self.head = n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="-->")
            temp = temp.next
    def dequeue(self):
        temp = self.head
        if self.head is None:
            print("The queue is empty")
        else:
            self.head = temp.next
            temp.next = None
q = queueSLL()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.display()

