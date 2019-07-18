class M:
    def sum(self):#method declaration
        #self keyword require objects
        pass
    def display(self):
            print("in parents class ")
        #N is a child class extending parent class M
        # pass keyword pass it no abstraction
   #m instance of class M
#m is an object of class calling default const
class N(M):
    def sum(self,a):
        print("inside sum of child class")
class J(N):
    def arc (self,a):
           print("inside class j arc")
    def sum(self):
        print("inside sum of arc")
#class Q(N,M,J):
   # pass
#m = N()
a= J()
a.sum()
a.display()
a.arc(18)
#q=Q()