for i in range(int(input())):
      z=int(input())
      m=[input().split() for j in range(z)]            
      m=[list(map(int,i))for i in m]
      ma=float('-inf')
      b=len(m[0])
      for j in range(b):
            q=[]
            bol=True
            for k in range(1,z):
                  if m[k][j]>m[k-1][j]:
                        q.append(m[k][j])
                  else:
                        bol=False
            if bol:
                  if ma<sum(q)+m[0][j]:
                        ma=sum(q)+m[0][j]
      print(ma if ma!=float('-inf') else -1 )
