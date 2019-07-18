class C:
    def __init__(self,age):
        self.__age=age
        #getter method
    def get_age(self):
        return self._age
    #setter method
    def set_age(self,x):
        self.__age=x
c=C()
c.set_age(20)
