class Node:
      def __init__(self,data):
          self.data=data
          self.next=None
class linked:
      def ins(self,head,data):
            if head==None:
                  head=Node(data)
                  return head
            else:
                  temp=head
                  while temp.next!=None:
                        temp=temp.next
                  temp.next=Node(data)
                  return head
      def dis(self,head):
            if head==None:
                  print("empty")
            else:
                  temp=head
                  while temp!=None:
                        print(temp.data)
                        temp=temp.next
      def dela(self,head):
            if head==None:
                 print("empty")
                 return None
            else:
                  temp=head
                  prev=None
                  while temp.next!=None:
                        prev=temp
                        temp=temp.next
                  del prev.next
                  prev.next=None
                  return head
head=None
a=linked()
head=a.ins(head,10)
a.dis(head)
head=a.ins(head,20)
head=a.ins(head,30)
head=a.ins(head,40)
head=a.ins(head,50)
head=a.ins(head,60)
head=a.ins(head,70)
head=a.dela(head)
a.dis(head)
