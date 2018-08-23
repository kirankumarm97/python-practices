from collections import defaultdict
def anagram(str1,str2):
      m=defaultdict(int)
      str1=str1.replace(' ','')
      str2=str2.replace(' ','')
      for i in str1:
            m[i]+=1
      for i in str2:
            m[i]-=1
      for i in m:
            if m[i]!=0:
                  print(1)
                  return False
      print(2)
      return True
            
anagram(input(),input())
