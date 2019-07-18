a=int(input("enter number"))
flag=0
for i in range(2,a):
     b=a%i
     if(b==0):
         flag=1

if(flag==1):
    print("not a prime number")
else:
    print("prime number")
