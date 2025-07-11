lists=list(map(int,input("ENter the number in list").split()))
positive=[]
for i in lists:
    if(i>0):
        positive.append(i)
print(positive)
