class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
    def __gt__(self,other):
        return self.area()>other.area()
    
r1=rectangle(33,3)
r2=rectangle(2,2)

if r1>r2:
    print("Area of r1 is greater")
else:
    print("Area of r2 is greater")
