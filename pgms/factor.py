import math
def perfect(n):
      a=[]
      for i in range(2,math.sqrt(n)+1):
            if n%i==0:
                  a.append(i):
      if sum(a)==n:
            return True
      return False
