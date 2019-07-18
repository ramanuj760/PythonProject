class Veichle:
    def acccelrate(self):
        print("accelrate the veichle")
    def brake(self):
        print("stop the veichle")
    def wheel(self):
        print("roatate wheel of veichle")
    def gearlock(self):
        print("gear lock")
    def seatbelt(self):
        pass
    def staring(self):
        pass
    def airbags(self):
        pass
    def seatbelt(self):
        pass
class Bike(Veichle):
    print("bike features")

class Car(Veichle):
    print("car feaure")
    def seatbelt(self):
        print("seatbelt available")
    def staring(self):
        print("staring ")
    def airbags(self):
        print("airbags")
c=Veichle
a=Bike()

a.wheel()
a.brake()
a.gearlock()
a.acccelrate()

b=Car()
b.acccelrate()
b.airbags()
b.gearlock()
b.brake()
b.staring()
b.wheel()


