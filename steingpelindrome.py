s=input("enter string value")
l=len(s)

p=""
for i in range(l-1,-1,-1):
    p=p+s[i]
print(p)
if(p==s):
    print("pelindrome")
else:
    print("not a pelidrome")