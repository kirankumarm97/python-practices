for i in range(int(input())):
    m,n=input().split()
    m,n=int(m),int(n)
    a=input().split()
    a=list(map(int,a))
    a*=n
    b=a[0]
    c=a[0]
    for i in a[1:]:
        if i >=-(10**6) and i<=(10**6):
            b=max(b+i,i)
            c=max(b,c)
    print(c)
