"""write a python program to convert tempratures to and from celcius fahrenheit"""
print("for calculate temprature in fahrenheit press f \n calculate temrature in celcius press c")
t=input("enter f or c:")
if t=='f':
    c=int(input("temp in celcius="))
    f=((9*c)/5)+32
    print(int(f),"f")
elif t=='c':
    f= int(input("temp in fahrenhite="))
    c=((f-32)/9)*5
    print(int(c),"c")
else:
    print("please enter for calculate temprature in f or c")