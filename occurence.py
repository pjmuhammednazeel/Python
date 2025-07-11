string=input("Enter the name")
freq={}
for char in string:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1
print(freq)
