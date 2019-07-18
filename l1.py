"""write a python program to sum all the item in a list"""
a=[25,6,19,15,34,69]
a.sort()
#print(len(a))
b=1
l=len(a)
for i in range(0,l):
    b=a[i]+b
print(b)
