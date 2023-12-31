class Magic:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
x=Magic(10)
y=Magic(20)