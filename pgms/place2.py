a=[[1,2,3,4],[2,3,4,5],[6,7,8,9],[6,7,8,4]]
def func(i,j,n):
      if i==n or j==0:
            print(a[i][j])
            return a[i][j]
      print(a[i][j])
      return  func(i,j-1,n)+a[i][j]+func(i+1,j,n)
sum=func(0,len(a)-1,len(a)-1)
print(sum)
      
