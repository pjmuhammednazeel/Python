lists=list(map(int,input("Enter numbers").split()))
new=[]
for i in lists:
    if(i%2==0):
        new.append(i)
print(new)
