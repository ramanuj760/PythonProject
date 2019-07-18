"""write a python program to guess a number between 1 to 9"""
from random import randint
r=randint(1,20)
flag=0
for i in range(9):
    a = int(input("enter user number"))
    if r==a:
        print("successful")
        break
    else :
        print("number is not equal enter number again")
print(r)


