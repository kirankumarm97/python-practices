from collections import Counter
if __name__ == "__main__":
    s = input().strip()
    b=[]
    a=Counter(s)
    for i in a.keys():
            b.append([i,a[i]])
    b=sorted(b,key=lambda x:(-int(x[1]),-ord(x[0])))[:3]
    for i in b:
        print(*i)
