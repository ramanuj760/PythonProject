class Over:
    def overloading_met(self,datatype,a=None,b=None,c=None):
        print("inside overloading ")
        print("Rcv datatype",datatype)
        if datatype=='int':
            e=a+b
            print(e)
        elif datatype=='str':
            d=a+b
            print(d)
o=Over()
o.overloading_met('int',123)
def OverArgs:
    def overload(self,datatype,*args):
        global answer
        answer=0
        if datatype=='int':
            answer=0
        elif datatype=='str':
            answer=" "
            for n in args:
                answer=answer+n
                print(answer)
over=OverArgs()
overa.overloa("int",2,4,5)

