def fib(n):
    i=0
    j=1
    for _ in range(n):
        print(i,j)
        t=i+j
        i=j
        j=t
    print(i)
fib(int(input()))
