
queue_1 = []
def Enqueue():
    if len(queue_1)==5:
        print("Queue is full")
    else:
        number = int(input("Enter the Number"))
        queue_1.append(number)

def Dequeue():
    if not queue_1:
        print("Empyt queue")
    else:
        queue_1.pop(0)
def Display():
    print(queue_1)


if __name__ == '__main__':
    while True:
        print("1:Enqueue \n2:Dequeue \n3:Display \n4:Break")
        opertion = int(input("Enter the number which opertion You want to perform"))

        if opertion==1:
            Enqueue()
        elif opertion==2:
            Dequeue()
        elif opertion==3:
            Display()
        elif opertion==4:
            break
        else:
            print("Wrong choice")
            break