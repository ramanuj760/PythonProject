class C:
    def __init__(self,age=0):
        self.__age=age # double under score means private and single under score are protected
#in encapsulation all member in private in nature and it contain getter and setter methods
#getter and setter method is equliproprotion no of variable in the class
   #getter method
    def get_age(self):
        return self.__age
    #settter method
    def set_age(self,x):
        self.__age= x
c=C()
c.set_age(26)
print(c.get_age())
class Overload:
    def __init__(self,a):
        self.a=a

