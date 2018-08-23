def func(a,b):
    if len(a)!=len(b):
        return False
    count=0
    for i in range(len(a)):
        if a==b[i:]+b[:i]:
            return count
        count+=1
print(func(input(),input()))
