"""write a program that accepts a word from the user and reverse it."""
x=input("enter a word")
l=len(x)
for i in range(l-1,-1,-1):
    print(x[i],end=" ")
print()
