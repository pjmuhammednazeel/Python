

lists=[]
f=open("file.txt","r")
for i in f:
    lists.append(i.strip())
f.close()
print(lists)
