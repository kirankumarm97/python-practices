from itertools import combinations_with_replacement
def func(a,b) :
    c=[]
    k=0
    for i in a :
        if i%b==0 :
            k+=1
    for i in range(1,len(a)+1):
        c.extend(list(combinations_with_replacement(a,i)))
    for i in c :
        if sum(i)==b:
            k+=1
    return k
n,m=map(int,input().split())
z=list(map(int,input().split()))
print(func(z,n))
