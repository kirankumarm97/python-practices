from itertools import combinations_with_replacement
a,b=input().split()
for i in list(combinations_with_replacement(sorted(a),int(b))):
    print(''.join(i))
