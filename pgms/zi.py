a,b=map(int,input().split())
z=list(input().split() for _ in range(b))
z=list(map(lambda x:[float(j) for j in x] ,z))
y=list(zip(*z))
for i in y:
    print(sum(i)/b)
