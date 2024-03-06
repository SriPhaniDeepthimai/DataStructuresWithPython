#Stack V01

S = []
Cap = 5
Top = 0
Bottom = 0

def pushStk(num):
    global Top
    global S
    if Top == Cap:
        print("Stack is Full")
        return
    S.append(num)
    Top += 1
def popStk():
    global Top
    if Top == Bottom:
        print("Stack is Empty")
        return
    print(f"{S[Top-1]} is popped out")
    Top -= 1

def printList():
    if Top == Bottom:
        print("Stack is Empty")
        return
    for i in range(Top-1,-1,-1):
        print(S[i])
if __name__ == "__main__":
    pushStk(10)
    pushStk(11)
    pushStk(12)
    pushStk(13)
    pushStk(14)
    pushStk(15)
    printList()
    popStk()
    popStk()
    popStk()
    popStk()
    popStk()
    popStk()
    popStk()
