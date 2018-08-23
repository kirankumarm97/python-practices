from collections import Counter,OrderedDict
if __name__ == "__main__":
    s = input().strip()
    b=[]
    a=Counter(s)
    for i in a.keys():
        if(a[i]>1):
            b.append([i,a[i]])
    b=sorted(b,key=lambda x:x[1])
    b.reverse()
    for i in b
        print(*i)
