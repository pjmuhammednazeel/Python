import csv

f=open("data.csv","r")
re=csv.reader(f)
for i in re:
    print(i)
f.close()
