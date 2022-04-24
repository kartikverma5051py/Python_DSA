class Node:
    def __init__(self,data):
        self.data = data
        self.address = None
class Slinkedlist:
    def __init__(self):
        self.head = None
    def printll(self):
        if self.head is None:
            print("Empty is Linked list")
        else:
            n = self.head
            while n is not None:
                print(n.data , "--> [link of next]",end= " ")
                n = n.address
    def add_after(self,data , value_after):
        n = self.head
        while n is not None:
            if value_after == n.data:
                break
            n = n.address
        if n is None:
                print("Linked list is Empty")
        else:
            new_data = Node(data)
            new_data.address = n.address
            n.address = new_data


if __name__ == '__main__':
    link1 = Slinkedlist()
    link1.head  = Node(10)
    link1.add_after(20,10)
    link1.printll()
