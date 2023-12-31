#In python the method overloading is not applicable
class Model:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def add(a,b,c):
        return a+b+c
obj=Model()
obj.add()