# class id:
#     "better one"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_set(self):
#         print(self.name)
#
#     def method(self):
#         print("method")
# a=id("ramanuj",30)
# a.method()
# print(a.__dict__)
# print(a.__doc__)
# print(a.__module__)
# print(id.__name__)

"""class M:
    def sum(self):
        pass
class N(M):
    def sum(self):
        print("sum of class")
m=N()
m.sum()"""
class Overloading:
    def overloading_a(self,datatype,a=None,b=None):
        if datatype=='int':
            c=a+b
            print(c)
        elif datatype=='str':
            d=a+b
            print(d)
o=Overloading()
o.overloading_a('int',5,6)
