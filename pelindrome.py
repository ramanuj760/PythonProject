print("check number is pelindrome or not")
n= int(input("enter number"))
pal=0
while n>0:
    r = n % 10
    pal=pal*10+r
    n=n//10
if(n==r):
    print("number is pelindrome")
else:
    print("number is not a pelindrome")