lists=list(map(int,input("ENter the numbers").split()))
new=[]
for i in lists:
    if i>100:
        new.append("over")
    else:
        new.append(i)
print(new)
