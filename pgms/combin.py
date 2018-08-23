from itertools import combinations
a,b=input().split()
c=[]
for i in range(1,int(b)+1):
    c.append(list(combinations(sorted(a),i)))
for i in c:
    for j in i:
        print(''.join(j))
