class X:
    def __init__(self):
        self.a=15
        self._b=20
w=X()
# print(w.__a) its shows error in python it shows no attribute due to secutriy reason
print(w._b)
