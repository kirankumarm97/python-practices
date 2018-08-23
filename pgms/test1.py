def fib(n):
    i=0
    j=1
    a=[]
    for _ in range(n):
        a.append(i)
        i,j=j,i+j
    return a
a=fib(100)
l=int(input())
while l:
    print(a[l])
    l=int(input())
