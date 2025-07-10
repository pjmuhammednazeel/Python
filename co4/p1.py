class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
        
l1=int(input("Enter length of rectangle1"))
b1=int(input("Enter breadth of rectangle1"))
l2=int(input("Enter length of rectangle2"))
b2=int(input("Enter breadth of rectangle2"))

r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
print("area of rectangle1=",r1.area());
print("area of rectangle2=",r2.area());

if r1.area()>r2.area():
    print("area of rectangle 1 is high")
elif r1.area()<r2.area():
    print("area of rectangle 2 is high")
else:
    print("both are equal")
