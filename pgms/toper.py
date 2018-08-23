c={}
for i in range(int(input())):
    a=input()
    b=float(input())
    c[a]=b
z=[]
a=list(c.values())
a=a[0]
for i in list(c.values())[1:]:
    if i<a:
        a=i
b=101
for i in list(c.values())[1:]:
    if i >a and i<b:
        b=i
for i in c:
    if c[i]==b:
        z.append(i)
print(*sorted(z),sep="\n")
