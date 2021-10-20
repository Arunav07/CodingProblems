#converting an integer to a list of digits

def NumList(n):
	l = []
	while(n>0):
		l.append(n%10)
		n = n//10
	z = []
	for i in range(len(l)):
		z.append(l[n-i-1])
	return z

print(NumList(int(input())))
