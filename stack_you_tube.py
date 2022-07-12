# stack = []
# def stackPush():
#     if size == len(stack):
#         print("Stack is full")
#     else:
#         item = input("Enter item in stack")
#         stack.append(item)
# def stackpop():
#     if not stack:
#         print("stack is Empty")
#     else:
#         itemPop = stack.pop()
#         print(itemPop)
# def displayStack():
#     print(stack)
#
# if __name__ == '__main__':
#     size = int(input("Enter the size of the stack"))
#     while True:
#         operation = """press
#         1 = push
#         2 = pop
#         3 = display Stack
#         4 = Exit
#         """
#         print(operation)
#         number = int(input("Enter operation which Yoy want to preform: "))
#         if number == 1:
#             stackPush()
#         elif number ==2 :
#             stackpop()
#         elif number == 3:
#             displayStack()
#         elif number == 4:
#             exit()
#         else:
#             print("Invalid number")


import collections
stack = collections.deque
import queue
stack = queue.LifoQueue(maxsize=10)
try:
    stack.put(10,timeout=1)

    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
    stack.put(10 , timeout=1)
except Exception as e:
    print(e)
finally:
    print("kartik")
print(stack.qsize())
print(stack.full())
print(stack)