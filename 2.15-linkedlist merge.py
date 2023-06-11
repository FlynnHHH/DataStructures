class Node:
   def __init__(self, dataval=None):
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

m, n = map(int, input().split())
dataa = list(map(int, input().split()))
datab = list(map(int, input().split()))
ha = SLinkedList()
hb = SLinkedList()
hc = SLinkedList()
ha.makelist(dataa)
hb.makelist(datab)
hc.headval = hb.headval
hc.gettail().nextval = ha.headval
hc.listprint()

