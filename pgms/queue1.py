class queue:
      def __init__(self):
            self.a=[]
            f=0
            r=-1
      def _insert(self,data):
            self.a.append(data)
      def _delete(self):
            f+1
      def _display(self):
            print(self.a[f:])
      def _is_empty(self):
            if len(self.a)==0:
                  return True
            else:
                  return False

que=queue()
while True:
      n=int(input())
      if n==1:
            
            que._insert(int(input()))
      elif n==2:
            if que._is_empty:
                  print("queue empty")
            else:
                  que._delete()
      elif n==3:
            que._display()
      else:
            break
                  
