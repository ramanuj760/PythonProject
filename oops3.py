
class A:
    "wwhat are you doing now"
    def __init__(self):
         print("constructor using cocept")
    def display1(self):
        print("hello ramanuj")


class B(A):
    print("inherite class of A")
a=A()
print(A.__doc__)
print(A.__dict__)
a.display1()