stack = []
def push_element():
    if len(stack) == size:
        print("Stack is full")
    else:
        elememt = input("Enter the Element")
        stack.append(elememt)
        print(stack)
def pop_element():
    if not stack:
        print("Stack is empty !")
    else:
        e = stack.pop()
        print("removed element :",e)
        print(stack)

size = int(input('Enter the size of stack '))
while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice  = int(input())
    if(choice == 1):
        push_element()
    elif choice ==2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation")
