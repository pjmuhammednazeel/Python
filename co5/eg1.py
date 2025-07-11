import csv
f=open("data.csv","w")
wr=csv.writer(f)

wr.writerow(["name","age","city"])

n=int(input("Enter the number of values:you have to enter"))

for i in range(n):
    name=input("Enter name")
    age=int(input("enter age"))
    city=input("ENter city")

    wr.writerow([name,age,city])
f.close()


f=open("data.csv","r")
re=csv.reader(f)

for i in re:
    print(row[1])
f.close()

