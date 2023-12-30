class Sbi:
    manger="Jagan"
    def __init__(self,name,mobile,acc,balance):
        self.name=name
        self.mobile=mobile
        self.account=acc
        self.balance=balance
    def credit(self,amount):
        self.balance+=amount
    def debit(self,amount):
        self.balance-=amount
    def update(self,mob):
        self.mobile=mob
    @classmethod    #Used to change the values in class objects
    def change_manger(cls,new):
        cls.manger=new
    @staticmethod# this method is a independent method which is used to assign values directly
    #without object address
    def add(a,b):
        return a+b

Chandra=Sbi('Nara Chandra',775757686,729732973,2)
Lokesh=Sbi('Nara Lokesh',879307362,9782397399,5)