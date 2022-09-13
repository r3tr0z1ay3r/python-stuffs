from tkinter import N
from numpy import delete


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end="==>")
                if temp.next == self.head:
                    break
                else:
                    temp = temp.next
    def insert_begin(self,data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            n.next = temp
            while temp.next != self.head:
                temp = temp.next
            temp.next = n
            print(temp.data)
            self.head = n
            #temp.next = self.head

    def insert_end(self,data):
        n = node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data)
                temp = temp.next
            print(temp.data)
            temp.next = n
            n.next = self.head
    def insert_any(self,data,pos):
        if self.head is None:
            print("The list is empty")
        else:
            n = node(data)
            temp = self.head
            try:
                for i in range(pos-1):
                    prev = temp
                    temp = temp.next
                prev.next =n
                n.next = temp
            except AttributeError:
                print("There is no position that is specified in the list")
            
            
    def delete_begin(self):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
        print(temp.data)
    def delete_end(self):
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head
        #temp.next = None
    def delete_any(self,pos):
        temp = self.head
        try:
            for i in range(0,pos-1):
                prev = temp
                temp = temp.next
            prev.next = temp.next
        except AttributeError:
            print("There is no position that is specified in the list")


n1 = node(10)
s = cll()
s.head = n1
n2 = node(20)
n1.next = n2
n2.next = n1
s.insert_begin(30)
#s.delete_any()
s.display()
