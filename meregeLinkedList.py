from Full_linked_list import Node,Linkedlist
def merge_List(firstList ,secondList,mergeList):

    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentFirst is None:
            mergeList.insert_End(currentSecond)
            break
        elif currentSecond is None:
            mergeList.insert_End(currentSecond)
            break
        elif currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mergeList.insert_End(currentFirst)
            currentFirst = currentFirstNext
        else:
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mergeList.insert_End(currentSecond)
            currentSecond= currentSecondNext


if __name__ == '__main__':
    nodeOne = Node(1)
    nodeTwo = Node(3)
    nodeThree = Node(4)
    firstList = Linkedlist()
    firstList.insert_End(nodeOne)
    firstList.insert_End(nodeTwo)
    firstList.insert_End(nodeThree)



    nodeFour = Node(2)
    nodeFive = Node(7)
    nodeSix = Node(9)

    secondList = Linkedlist()
    secondList.insert_End(nodeFour)
    secondList.insert_End(nodeFive)
    secondList.insert_End(nodeSix)


    print("Printinf First List")
    firstList.printlist()
    print()

    print("Printing second list")
    secondList.printlist()
    print()
    mergeList = Linkedlist()

    merge_List(firstList,secondList,mergeList)
    print("Merege List ")
    mergeList.printlist()