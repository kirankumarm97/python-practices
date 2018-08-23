class node:
      def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None
def bst(root,data):
      if not root:
            return node(data)
      if root.data>data:
            root.left=bst(root.left,data)
      elif root.data<data:
            root.right=bst(root.right,data)
      return root
a=[]
def dis(root):
      if root:
            dis(root.left)
            print(root.data)
            dis(root.right)
for i in range(int(input())):
      a.append(int(input()))
root=None
for i in a:
      root=bst(root,i)
dis(root)
