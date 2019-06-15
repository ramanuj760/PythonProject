#arithmetic operator
print("we are performing arithmetic operator")
print("enter a among them operator +,-,*,/,%:")
a= (input())
print("enter a first number")
c=float(input())
print("enter a second number")
b = float(input())
print()

if a=='+':

    print(c,'+',b,"=",c+b)
elif a=='-':
    print(c,'-',c-b)
elif a=='*':
    print(c,'*',c*b)
elif a=='/':
    print(c,'/',c/b)
elif a=='%':
    print(c,'%',b,"=",c%b)
elif a=="//":
    print(c,"//",b,"//",c//b)

else :
    print("operation perform above these")