print("write a python program to print alphabeet pattern z")
m=1
n=4
for i in range(0,6):
    for j in range(0,5):
        if(i==0 or i==5):
            print("*",end=" ")
        elif(i==m and j==n):
            print("*", end=" ")
            m=m+1
            n=n-1
        else:
            print(end=" ")
    print()