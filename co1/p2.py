cy=int(input("enter current year"))
fy=int(input("enter final year"))

for i in range(cy,fy+1):
    if(i%400==0)or(i%4==0 and i%100!=0):
        print(i)
