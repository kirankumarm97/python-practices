list1=[]
def perfect(n):
	a=int(n/2)
	for i in range(1, a+1):
		if n%i==0:
			list1.append(i)
	print(list1)
	print(sum(list1[0:len(list1)-1]))
	if sum(list1[0:len(list1)])==n:
		return True
	else:
		return False
