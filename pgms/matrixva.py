z=[]
def func(a,k,l):
      n=len(a)
      su=0
      i=0
      j=0
      x=l
      for j in range(l+1):
          su+=a[i][j]
          print(a[i][j])
      i=1
      #print(l)
      if l!=n-1:
          for i in range(1,k+1):
                su+=a[i][j]
                print(a[i][j])
          for x in range(l+1,n):
                su+=a[i][x]
                print(a[i][x])
      print('x',x,i)
      if  i !=n-1:
          for y in range(i+1,n):
                su+=a[y][x]
                print(a[y][x])
      z.append(su)
a=[[1,7,5,17],[2,5,12,19],[3,9,23,2],[4,10,13,1]]
func(a,1,0)
print(z)
