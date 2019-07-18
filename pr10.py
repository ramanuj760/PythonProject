"""armstrong number"""
a= int(input("enter number"))
l=len(str(a))
arm=0
while a>0:
    r=a%10
    arm=arm+r**l
    a=a//10
if(arm==a):
    print("successful")
else:
    print("unsuccess")