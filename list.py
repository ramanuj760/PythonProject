l=[]
print(l)
l.append(22)
print(l)
l.insert(1,99)
print(l)
l[1]=55
print(l)
a=[33,96,56,75,96]
b=['ram','Python','HELLO','List']
a.insert(2,57)
print(a)
print(b)
print(max(a))
print(min(a))
a.sort()
print(a)
a.sort(reverse=True) #decreasing order
print(a,"reverse")
b.sort()
print(b)
b.sort(key=str.lower)
print(b,"yes  ")
print(b.index('Python'))
a.remove(96) # if more than value it remove first instance
print(a)
c=a*2
print(c)# list shows multiple list
d=[a,b]
print(d)
print(d[0][1])
print(list(range(10)))
print(list("hello"))
print('ram'in b[1])
print(a)
del a[1]
x=[44,63,96,44,]
print(x)
print(x.count(44))
(x.pop())# element remove from end if value notgiven if value is given it remove only that value
print(x)
a=[94,66,34,52,88,76]
a.sort()
print(len(a))
f=a[:3]
print(f)
g=a[2:]
print(g)
h=a[2:5]
print(h)

# for n in range (a):
#     print(n)
# for n in range (len(a)):
#     print(n)
