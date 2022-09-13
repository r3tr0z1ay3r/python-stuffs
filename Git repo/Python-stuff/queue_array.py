class queue:
    def __init__(self,que):
        self.que = que
    def enque(self,data):
        self.que.append(data)
    def dequeue(self):
        self.que.pop(0)
    def display(self):
        print(self.que)

q = [1,2,3,4,5]
que = queue(q)
que.enque(6)
que.dequeue()
que.display()
