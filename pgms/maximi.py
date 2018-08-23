a,b=list(map(int,(input().split())))
c=[]
for i in range(a):
    c.append(list(map(int,(input().split()))))
    d=[]
for i in range(a):
    d.append(max(c[i]))
e=sum(list(map(lambda x:x*x,d)))
print(e%b)
