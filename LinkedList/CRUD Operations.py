
#LINKED LIST INSERTION,DELETION,APPEND NODE
class Node:
    def __init__(self,num=0):
        self.data=num
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
        self.count=0
        self.max=0
        self.max1=0
    def appendNode(self,num=0):
        nn=Node(num)
        nn.data=int(input("Enter the node value: "))
        if self.head==None:
            self.head=nn
            self.temp=self.head
            self.count+=1
        else:
            while(self.temp.next!=None):
                self.temp=self.temp.next
            self.temp.next=nn
            self.count+=1
    def DeleteNode(self,val=0):
        val=int(input("Enter data you want to delete: "))
        self.prev=self.head
        self.temp=self.prev.next
        if self.head.data==val:
            self.head=self.temp
        else:
            while(self.temp!=None):
                if self.temp.data==val:
                    self.prev.next=self.temp.next
                self.prev=self.prev.next
                self.temp=self.temp.next
    def DeletingUsingIndex(self,po=0):
        self.prev=self.head
        self.temp=self.prev.next
        if po==1:
            self.head=self.temp
        for i in range(2,self.count+1):
            if po==i:
                self.prev.next=self.temp.next
            self.prev=self.prev.next
            self.temp=self.temp.next
                
            
    def ReverseList(self):
        self.prev = None
        self.temp = self.head
        while (self.temp!=None):
            nnode = self.temp.next
            self.temp.next =self.prev
            self.prev = self.temp
            self.temp = nnode
        self.head = self.prev
        
     #BubbleSort   
    def sortLL(self):
        self.prev=self.head
        for i in range(1,self.count):
            self.temp=self.prev.next
            while self.temp:
#                 print(f"slow:{self.prev.data} and fast:{self.temp.data}")
                if self.prev.data>self.temp.data:
                    self.prev.data,self.temp.data=self.temp.data,self.prev.data
                self.temp=self.temp.next
            self.prev=self.prev.next
            
    #InsertionSort
    def Insertionsort(self):
        self.prev=self.head
        self.temp=self.prev.next
        for i in range(0,self.count):
            key=self.temp.data
            j=i-1
            while(j>=0 and key<self.prev.data):
                self.temp.data=self.prev.data
                j-=1
            self.temp.data=key
            
    def Max_difference(self):
        self.sortLL()
        print("After sorting: ")
        self.prev=self.head
        self.temp=self.prev.next
        if self.count<2:
            return 0
        else:
            while(self.temp):
                self.max=self.temp.data-self.prev.data
                if(self.max1<self.max):
                    self.max1=self.max
                self.temp=self.temp.next
                self.prev=self.prev.next
                
            print(self.max1)
            
            
    def Count(self):
        print(self.count)
            
    def printList(self):
        self.temp=self.head
        while(self.temp!=None):
            print(self.temp.data,end="->")
            self.temp=self.temp.next
            
        print("None")
    
                
if __name__=="__main__":
    LL=LinkedList()
    LL.appendNode()
    LL.appendNode()
    LL.appendNode()
    LL.appendNode()
#     LL.appendNode()
#     LL.appendNode()
#     LL.appendNode()
    LL.printList()
#     LL.Majority_element()
    LL.Count()
#     LL.printList()
#     LL.DeleteNode()
#     LL.printList()
#     LL.DeleteNode()
#     LL.printList()
#     LL.ReverseList()
#     LL.printList()
#     LL.DeletingUsingIndex(5)
#     LL.printList()
#     LL.DeletingUsingIndex(3)
#     LL.printList()
#     LL.sortLL()
    LL.Max_difference()
