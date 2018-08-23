t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    for i in range(n-1):
        for j in range(i+1,n):
            print(i,j)
            if a[i]+a[j]==m:
                print(i+1,j+1,'hello')
