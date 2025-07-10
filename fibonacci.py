n=int(input("Enter the number"));
t1=0
t2=1
nt=t1+t2
print(t1);
print(t2);
for i in range(3,n+1):
	print(nt);
	t1=t2
	t2=nt
	nt=t1+t2

