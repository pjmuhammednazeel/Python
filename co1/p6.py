lists = input("Enter first names: ").split()
count = 0

for name in lists:
    if name[0].lower() == 'a':
        count += 1

print("Number of names starting with 'a':", count)

