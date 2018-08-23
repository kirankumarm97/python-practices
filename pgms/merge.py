def func1(a,l,h):
    if(l>=h):
        return
    mid=(l+h)//2
    func1(a,l,mid)
    func1(a,mid+1,h)
    func2(a,mid,l,h)
def func2(a,mid,l,h):
    i=l
    j=mid+1
    k=0
    c=[0]*(h-l+1)
    while(i<=mid and j<=h):
        if(a[i]<a[j]):
            c[k]=a[i]
            i+=1
            k+=1
        else:
            c[k]=a[j]
            j+=1
            k+=1
    while i<=mid:
        c[k]=a[i]
        i+=1
        k+=1
    while j<=h:
        c[k]=a[j]
        j+=1
        k+=1
    for i in c:
        a[l]=i
        l+=1
a=list(map(int,input().split()))
func1(a,0,len(a)-1)
print(a)
