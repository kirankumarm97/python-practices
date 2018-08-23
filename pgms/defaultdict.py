from collections import defaultdict
a,b=map(int,input().split())
c=[]
d=[]
e=0
for i in range(a):
    c.append(input())
for _ in range(b):
    d.append(input())
for i in range(len(d)):
    e=0
    for j in range(len(c)):
        try:
            e=c.index(d[i],e)
            e+=1
            print(e,end=" ")
        except ValueError:
            if e==0:
                print(-1,end=' ')
            
            break  
    print()
