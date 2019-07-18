class A:
    #print("this is a parent class")
    #d={"name":"ram"}
    "this is a sample string"
    def __init__(self):
        print("inside construcor")
    def display(self):
            print("inside method")

class B(A):
    pass
#a is an instance of class A. A() is an object of class A
#calling a default constructor
#b=B()
a=A()
print(a.__doc__)# print the string of class which are not in print
print(A.__dict__)# it gives all the details of class
print(A.__module__)
print(A.__name__)
a.display()