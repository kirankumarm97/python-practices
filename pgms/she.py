import shelve
a=[1,2,3,4,5]
b=shelve.open("a")
b["mm"]=a
bl=[*b["mm"]]
print(b)
