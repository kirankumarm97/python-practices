def bub(a,l,h,z):
      mid=(l+h)//2
      if l>=h:
            return l
      if a[mid]==z:
            return mid+1
      elif z>a[mid]:
            return bub(a,mid+1,h,z)
      else:
            return bub(a,l,mid,z)
n = int(input())
a = []
t=0
for i in range(n):
    z=int(input())
    j=0
    a.insert(bub(a,0,t,z),z)
    t+=1
    if t%2!=0:
        print(float(a[t//2]))
    else:
        n=t//2
        print(float(sum(a[n-1:n+1])/2))
