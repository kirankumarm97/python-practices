class stack:
    def __init__(self):
        self.item=[]
    def push(self,a):
        self.item.append(a)
    def pop(self):
        self.item.pop()
    def top(self):
        print(self.item[len(self.item)-1])
    def print(self):
        print(self.item)
s=stack()
while True:
    a=int(input())
    if a==1:
        s.push(int(input()))
    elif a==2:
        s.pop()
    elif a==3:
        s.top()
    elif a==4:
        s.print()
    else:
        break
