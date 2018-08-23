def curency(costs,n):
      list1=[0 for _ in range(n+1)]
      list1[0]=1
      for cost in costs:
            for i in range(cost,n+1):
                  list1[i]+=list1[i-cost]

      print(list1[n])
curency([2,3,4],14)
