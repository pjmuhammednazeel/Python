#create a file and write
name=input("Enter the name of file")
f=open(name,"x")
f.close()
f=open(name,"w")
data=input("Enter the data to be inserted")
f.write(data)
f.close()

