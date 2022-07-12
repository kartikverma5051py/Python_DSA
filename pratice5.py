# class Node:
#     next: None
#
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     def __repr__(self):
#         return self.data
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def __repr__(self):
#         node = self.head
#         nodes =[]
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -->".join(nodes)
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
#
#
# if __name__ == '__main__':
#     llist = LinkedList()
#     # print(llist)
#     firstNode = Node("kartik")
#     llist.head = firstNode
#     # print(llist)
#     secondNode = Node("Anushka")
#     thirdNode = Node("kristine")
#     firstNode.next = secondNode
#     secondNode.next = thirdNode
#     # print(llist)
#     for node in llist:
#         print(node)
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def llistLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length
    def InsertHead(self,newNode):
        temporaryNode: object = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode
    def InsertInbetween(self,newNode,postion):
        if postion == 0:
            self.InsertHead(newNode)
            return

        if postion == self.llistLength():
            self.InsertEnd(newNode)
            return
        if postion<0 or postion>self.llistLength():
            print("Please Enter the valid index")
            return

        currentNode = self.head
        currentPostion = 0
        while True:
            if currentPostion == postion:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode =currentNode.next
            currentPostion +=1


    def InsertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode


    def __repr__(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data,"-->" ,end=" ")
            currentNode = currentNode.next
    def deleteHead(self):
        if self.llistLength()!=0:
            previousHead = self.head
            self.head=self.head.next
            previousHead.next =None
        else:
            print("Lindked List is empty.Delete Failed")

    def deleteINBetween(self,position):
        if position<0 or position>self.llistLength():
            print("Invalid Position")
            return
        elif position == 0:
            self.deleteHead()
            return
        elif position==self.llistLength():
            self.deleteEnd()
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition+=1

    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode=lastNode.next

        previousNode.next=None


if __name__ == '__main__':
    firstNode = Node("John")
    llist = LinkedList()
    llist.InsertEnd(firstNode)
    secondNode = Node("Kartik")
    llist.InsertEnd(secondNode)
    # (llist.__repr__())
    thirdNode = Node("Anushka")
    llist.InsertHead(thirdNode)
    forthNode = Node("Arpita")
    llist.InsertInbetween(forthNode,3)
    # llist.deleteHead()
    # llist.deleteEnd()
    llist.deleteINBetween(0   )
    llist.__repr__()

# import math
#
# n= 123
# sum = 0
# for i in range(len(str(n))):
#     result = n%10
#     sum = sum*10+result
#     n  = n//10
# print(sum)
# print(5//2)
# print(math.ceil(45.1))
#
# lst = [1,2,3,4,5,6,7]
# a = len(lst)//2
# temp = 0
# for i in range(a):
#     temp = lst[i]
#     lst[i] = lst[len(lst)-i-1]
#     lst[len(lst) - i - 1] =temp
# for i in range(len(lst)-1):
#     print(lst[i],end=" ")

# x= 1
# while x<=3:
#     print(x,end=" ")
#     x+=1
# else:
#     print(x)
#



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Problem>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class Solution:
#     def searchInsert(self, arr, target):
#
#
#
#
#         mid = len(arr)//2
#         if arr[mid]<=target:
#             result = 0
#             for i in range(len(arr[mid:])):
#                 if arr[mid]==target:
#                     result= mid
#                 elif arr[i]==target or target<arr[i+1]:
#                     result= mid+i
#                 elif (target>arr[i]):
#                     result = mid+i+1
#             return result
#         else:
#             result = 0
#             for i in range(len(arr[0:mid])):
#                 if arr[i]==target:
#                     result= i
#                 elif (arr[i]<target<arr[i+1]):
#                     result = i+1
#             return result
#
#
# obj = Solution()
# print(obj.searchInsert( [1,3,5,6],7))
# print(1//2)

