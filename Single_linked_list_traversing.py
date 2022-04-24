# Traversing a Linked List


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


class Linked_list:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data ,"-->",n.ref)

                n = n.ref





if __name__ == '__main__':




    list1 = Linked_list()
    list1.head = Node(10)
    item1 = Node(20)
    item2 = Node(30)
    list1.head.ref = item1
    item1.ref = item2
    list1.print_LL()




