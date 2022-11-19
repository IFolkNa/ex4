from math import pi

class Box():
    def __init__(self,Radius,Height) -> None:
        self.Radius = Radius
        self.Height = Height
Box1 = Box(Radius=5,Height=10)
volum = pi*Box1.Radius*Box1.Height
print("Volum of Box1 =:",volum)
Box2 = Box(Radius=7,Height=13)
volum2 = pi*Box2.Radius*Box2.Height
print("Volum of Box2 = :",volum2) 

def triangle(n):

    k = n - 1

    for i in range(0, n):
 
        for j in range(0, k):
            print(end=" ")

        k = k - 1
 
        for j in range(0, i+1):
         
            print("* ", end="")
        print("\r")
 
n = 17
triangle(n)
class pyramid():
    pyramid_length = ""
    pyramid_with = ""
    pyramid_height = ""
    def calculaotor(self):
        stack = (self.pyramid_length.i_length*self.pyramid_with.i_width*self.pyramid_height.i_height)/3
        print(stack)
        
class pyramidlength():
    i_length = ""
class pyramidwidth():
    i_width = ""
class pyramidheight():
    i_height = ""
Pyramid = pyramid()
pyramid1length = pyramidlength()
pyramid1width = pyramidwidth()
pyramid1height = pyramidheight()
pyramid1length.i_length = 10
pyramid1width.i_width = 7
pyramid1height.i_height = 17
Pyramid.pyramid_length = pyramid1length
Pyramid.pyramid_height = pyramid1height
Pyramid.pyramid_with = pyramid1width
Pyramid.calculaotor()

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval ,end = "->")
         printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode
    def RemoveNode(self, Removekey):
        HeadVal = self.headval  
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.head = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
                if HeadVal.dataval == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None

linklist = SLinkedList()
linklist.headval = Node(44)
Node1 = Node(36)
Node2 = Node(90)
Node3 = Node(10)
Node4 = Node(60)
Node5 = Node(99)

linklist.headval.nextval = Node1
Node1.nextval = Node2
Node2.nextval = Node3
Node3.nextval = Node4
Node4.nextval = Node5
linklist.AtBegining(104)
linklist.AtEnd(57)
linklist.RemoveNode(10)
linklist.listprint()