list1 = ["Red", "Green", "Blue", "Yellow"]
list2 = ["Green", "Yellow", "Black"]
new=[]
for i in list1:
    if i not in list2:
        new.append(i)
print(new)
