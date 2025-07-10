class publisher:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print("name=",self.name)
        
    
    
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        
    def display(self):
        super().display()
        print("title=",self.title)
        print("author=",self.author)
        
        

class python(book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price=price
        self.pages=pages
    
    def display(self):
        super().display()
        print("price=",self.price)
        print("pages=",self.pages)
        
        
name=input("Enter name of publisher")
title=input("ENter title")
author=input("Enter author")
price=int(input("enter price"))
pages=int(input("Enter pages"))

p1=python(name,title,author,price,pages)
p1.display()
