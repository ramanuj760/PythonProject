# class Over:
#     def overloading_met(self,datatype,a=None,b=None,c=None):
#         print("Inside overloading")
#         print("Rcv datatype ",datatype)
#         if datatype=='int':
#             e=a+b+c
#             print(e)
#         elif datatype=='str':
#             d=a+b+c
#             print(d)
#
#
# o=Over()
# o.overloading_met("int",2,3)

class OverArgs:
    def overloa(self,datatype,*args):
        global answer
        answer=0
        if datatype=='int':
            answer=0
        elif datatype=='str':
            answer=" "
        for n in  args:
            answer=answer+n
        print(answer)

overa=OverArgs()
overa.overloa("int",2,4,5)