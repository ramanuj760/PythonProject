class M:
    # method declaration
    def sum(self):
        pass
    def display(self):
        print("Isnide Parent display")
# N is a child class extending parent class M
class N(M):
    def sum(self):
        print("Inside sum of child class")

class J(N):
    def arc(self,a):
        print("Inside class J arc")
        print(a)
    def sum(self):
        print("Inside sum of arc")

#class Q(N,M,J):
    #pass

# m is an instance of class M
#M() an object of a class calling a default constructor
#a=N()
a=J()
a.sum()
a.display()
a.arc(18)

#w=Q()

