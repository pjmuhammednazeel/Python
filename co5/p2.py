f=open("file.txt","r")
j=1
d=open("new.txt","a")
for i in f:
    if(j%2!=0):
        d.write(i)
    j=j+1

d.close()
f.close()

d=open("new.txt","r")

print(d.read())

d.close()
