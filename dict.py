"""write a python program to guess number between 1 to 9"""
print("welcome in guess number")
import random

a= random.randint(1,20)
for i in range(9):
  b = int(input("enter a value"))
  if b<a:
    print("user value is small value")
  elif b>a:
    print(" user value is greater values ")
  else:
      break
print("value given by user",b)
if a==b:
    print("both the values are equal")
print("guessed number",a)
