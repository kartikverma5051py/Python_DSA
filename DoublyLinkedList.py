class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def print_ll_forward(self):
        print()
        if self.head is None:
            print("Linked List is empty !")

        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end= "")
                n = n.nref
            print( )
    def print_ll_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty !")

        else:
            n=self.head
            while n.nref is not None:
                # print(n.data,"-->",end= "")
                n = n.nref
            while n is not None:
                print(n.data,"-->",end= "")
                n = n.pref
            print()
    def insert_Empty(self,data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print('Linked is not empty')

    def insert_AtBegin(self,data):
        if self.head is None:
            self.head.insert_empty(data)
        else:
            newNode = Node(data)
            newNode.nref = self.head
            self.head.pref = newNode
            self.head = newNode

    def insert_InEnd(self,data):

        if self.head is None:
            self.head.insert_empty(data)
        else:
            newNode = Node(data)
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref= newNode
            newNode.pref = n

dll = DoublyLL()
dll.insert_Empty(10)
dll.insert_AtBegin(100)
dll.insert_AtBegin(100)
dll.insert_AtBegin(100)
dll.insert_InEnd(20)
dll.insert_InEnd(200)
dll.insert_InEnd(2000)


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<This is a result of forward>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
dll.print_ll_forward()
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<This is result a reverse>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
dll.print_ll_reverse()
dict1 = {"key1" :1,"key2":2}
dict2 = {"key2" :2,"key1":1}
print(dict1==dict2)





















