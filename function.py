a=25 #global variable
def display():
    a=64 # local for display but global sum that to be global
    print(a)
display()
print(a)
def sum():
    a=45
    print("inside second function",a)
sum()
print(a)