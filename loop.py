#using for loop giving multiplication table 2 to input value given by user
print("input value for multiplication table ")
a= int(input())
for i in range (2,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
