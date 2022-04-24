# <---------------- Insertion in a Linked List-------------------->


#         <---------Inserting at  End------------->

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Slinkedlist:
    def __init__(self):
        self.head = None
    def printll(self):
        if self.head is None:
            print("Empty linked list ")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", n.ref)

                n = n.ref
    def atEnd(self,newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        else:
            last_at = self.head
            while last_at.ref is not None:
                last_at = last_at.ref
        last_at.ref =newNode



if __name__ == '__main__':
    list1 = Slinkedlist()
    list1.head = Node("Mon")
    item2 = Node("Tue")
    item3  = Node("Wed")
    list1.head.ref = item2
    item2.ref = item3
    list1.atEnd("Thu")
    list1.printll()