print("welcome in guess number")
import random

a= random.randint(1,20)
for i in range(4):
  b = int(input("enter a value"))
  if b<a:
    print("its right it is small value")
  elif b>a:
    print(" greater value5 ")
  else:
      break
print("value given by user",b)
if a==b:
    print("both the values are equal")
print("guessed number",a)
