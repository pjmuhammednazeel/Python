class bank:
    def __init__(self,acno,name,typ,bal):
        self.acno=acno
        self.name=name
        self.typ=typ
        self.bal=bal
    
    def deposit(self,amt):
        self.bal=self.bal+amt
        print("Amount is deposited")
    
    def withdraw(self,amt):
        if amt>self.bal:
            print("Dont have sufficient balance")
        else:
            self.bal=self.bal-amt
            print("Amount withdrawn successfully")
    
    def display(self):
        print("name=",self.name)
        print("acno=",self.acno)
        print("type=",self.typ)
        print("bal=",self.bal)

acno=int(input("Enter the acno"))
name=input("Enter the name")
typ=input("Enter the typ")
bal=int(input("Enter the bal"))

b1=bank(acno,name,typ,bal)

while True:
    print("1.display")
    print("2.deposit")
    print("3.withdraw")
    print("4.exit")
    
    op=int(input("Enter option"))
    
    if op==1:
        b1.display()
    elif op==2:
        amt=int(input("Enter the amount to be deposited"))
        b1.deposit(amt)
    elif op==3:
        amt=int(input("Enter the amount to be withdrawn"))
        b1.withdraw(amt)
    elif op==4:
        break
    else:
        print("Invalid ")
