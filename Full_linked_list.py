class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def is_List_Empty(self):
        if self.head is None:
            return True
        else:
            return False
    """Length of linkedlist """
    def length_linkedlist(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            currentNode = currentNode.next
            count+=1
        return count
    """ Inserting node at the begining of the node """
    def insert_at_Begining(self,newnode):
        newnode.next = self.head
        self.head = newnode
    """ Inserting node at th end of the node """
    def insert_End(self, newNode):
        if self.head is None:
            self.head =newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next=newNode
    """ Inserting node in between in the linkedlist """
    def insert_IN_between(self,newNode,position):
        if position<0 or position >self.length_linkedlist():
            return f"Invalid Position {position}"
        if position == 0:
            self.insert_at_Begining(newNode)
            return
        if position == self.length_linkedlist():
            self.insert_End(newNode)
            return


        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition==position:
                perviousNode.next = newNode
                newNode.next = currentNode
                break
            perviousNode =currentNode
            currentNode = currentNode.next
            currentPosition+=1
    """ Deleting start of the node """
    def delete_Head(self):
        if self.is_List_Empty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            return "Linked list is empty . Delete Failed"

    """Deleting the node in between position """
    def deleteAt(self,position):
        if position<0 or position>=self.length_linkedlist():
            return f"Invalid position {position}"
        elif self.is_List_Empty() is False:
            if position == 0:
                self.delete_Head()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode=currentNode.next
                currentPosition+=1

    """Delete the Node for end of the node """
    def deleteEnd(self):
        lastNode =self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next=None

    def __repr__(self):
        currentNode = self.head
        result = []
        while currentNode is not None:
            result.append(currentNode.data)
            currentNode=currentNode.next
        result1 = list(map(str,result))
        return "->".join(result1)
    def printlist(self):
        if self.head is None:
            return "Empty linked list"
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data,end="->")
            currentNode=currentNode.next
if __name__ == '__main__':
    firstNode = Node("Kartik Verma")
    llist = Linkedlist()
    llist.insert_at_Begining(firstNode)
    secondNode = Node("kendall")
    firstNode.next = secondNode

    thirdNode = Node("kristein")
    llist.insert_End(thirdNode)
    fourthNode = Node("kylie")
    fivethNode = Node("Arpita")
    llist.insert_End(fourthNode)
    llist.insert_End(fivethNode)
    print(llist.printlist())
    llist.deleteAt(2)


    print(llist.printlist())
    llist.deleteEnd()
    print(llist)
    print(llist.length_linkedlist())

