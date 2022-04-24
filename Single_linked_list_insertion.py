
# <---------------- Insertion in a Linked List-------------------->


#         <---------Inserting at the Beginning------------->

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

    def insert_at_begining(self,newData):

        newNode = Node(newData)
        newNode.ref = self.head
        self.head = newNode



if __name__ == '__main__':




    list1 = Linked_list()
    list1.head = Node("Feb")
    item1 = Node("March")
    item2 = Node("April")
    list1.head.ref = item1
    item1.ref = item2
    list1.print_LL()

    print("Insertion at begining")
    list1.insert_at_begining("Jan")
    list1.print_LL()





