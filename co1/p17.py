n=int(input("Enter the limit"))
d={}
for i in range(1,n+1):
    key=input("Enter key value")
    value=input("ENter value")
    d[key]=value
print(d)
asce=dict(sorted(d.items()))
desc=dict(sorted(d.items(),reverse=True))
print(asce)
print(desc)
