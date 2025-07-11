word=input("enter the word")
vowels="aeiouAEIOU"
lists=[]
for i in word:
    if i in vowels:
        lists.append(i)
        
print(lists)
