n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
m=0
for i in range(n-1):
    for j in range(i+1,n):
        if abs(a[i]-a[j])<2:
            m+=1
            break
print(m)
