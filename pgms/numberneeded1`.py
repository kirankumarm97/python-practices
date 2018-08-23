def number_needed(a, b):
    z=0
    m=[i for i in a]
    for i in m:
        print('1')  
        if i in b:
            a.remove(i)
            b.remove(i)
        else:
            z+=1
    n=[i for i in b]  
    for i in n:
        if i in a:
            b.remove(i)
            a.remove(i)
        else:
            z+=1
    return z
import textwrap
a = textwrap.wrap(input(),1)
b = textwrap.wrap(input(),1)
print(number_needed(a, b))
