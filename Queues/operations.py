Q = []
Cap = 5
Rear = 0
Front = 0


def enqueueEle(num):
    global Rear
    global Q
    if Rear == Cap:
        print("Queue is Full")
        return
    Q.append(num)
    Rear += 1


def dequeue():
    global Front
    global Rear
    if Front == Rear:
        if (Rear == Cap):
            Front = 0
            Rear = 0
        print("Queue is Empty")
        return
    print(f"{Q[Front]} element is dequeued")
    Front += 1


def printList():
    if Front == Rear:
        print("Queue is Empty")
        return
    print("Queue is")
    for i in range(Front, Rear, 1):
        print(Q[i], end=" ")
    print()


if __name__ == "__main__":
    enqueueEle(10)
    enqueueEle(20)
    enqueueEle(30)
    print(Q)
    printList()
    dequeue()
    dequeue()
    printList()
    dequeue()
    dequeue()
