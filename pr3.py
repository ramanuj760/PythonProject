"""write a program to construct the following pattern using nested for loop"""
a=int(input("enter "))
for i in range(1,a+1):
    for j in range(1 ,i+1):
         print("*",end=" ")
    print()
for i in range(a,1,-1):
    for j in range(i,1,-1):
        print("*",end=" ")
    print()