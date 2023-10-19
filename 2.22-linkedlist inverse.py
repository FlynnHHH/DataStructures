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
        else: 
            printval = self.headval
            while printval is not None:
                print (printval.dataval, end = '')
                if printval.nextval is not None:
                    print(',', end = '')
                printval = printval.nextval
            print()
    
    def gettail(self):
        tail = self.headval
        while tail.nextval is not None:
            tail = tail.nextval
        return tail
    
    def inverse(self):
        if self.headval is None:
            return
        current = self.headval
        previous = None
        while current is not None:
            next = current.nextval
            current.nextval = previous
            previous = current
            current = next
        self.headval = previous
        return
    
lst = SLinkedList()
data = list(map(str, input().split(',')))
lst.makelist(data)
lst.inverse()
lst.listprint()
    