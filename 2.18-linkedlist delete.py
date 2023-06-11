class Node:
   def __init__(self, dataval = None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
       self.headval = None
    
    def makelist(self, data):
        for i in range(len(data)):
            self.append(data[i])
            
    def append(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode 

    def listprint(self):
        if self.headval is None:
            print("NULL")
            return
        printval = self.headval
        while printval is not None:
            print (printval.dataval, end = ' ')
            printval = printval.nextval
        print()
    
    def gettail(self):
        tail = self.headval
        while tail.nextval is not None:
            tail = tail.nextval
        return tail
    
    def delete(self, position):
        if position == 0:
            self.headval = self.headval.nextval
            return
        current = self.headval
        for i in range(position - 1):
            current = current.nextval
        current.nextval = current.nextval.nextval

data = list(map(int, input().split()))
list = SLinkedList()
list.makelist(data)
list.delete(int(input()))
list.listprint()
    