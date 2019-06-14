print("welcome in calculator ")
print("enter a operator +,-,*,/,%:")
a= (input())
print("enter a first number")
c=int(input())
print("enter a second number")
b = int(input())
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

else :
    print("operation perform above these")