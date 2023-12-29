class Sbi:
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
Chandra=Sbi('Nara Chandra',775757686,729732973,2)
Lokesh=Sbi('Nara Lokesh',879307362,9782397399,5)