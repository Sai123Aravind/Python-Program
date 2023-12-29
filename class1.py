class Employee:
    company='Tesla'
    ceo='Elon Musk'

    def insert (self,name,age,salary,eid):
        self.name=name
        self.age=age
        self.salary=salary
        self.eid=eid
        
Bhanu= Employee()
Bindu=Employee()  
Dhoni=Employee()      
Employee.insert(Bhanu,'Bhanu',22,50000,2102)
Employee.insert(Bindu,'Bindu',21,40000,2103)
Dhoni.insert("Mahendra Singh Dhoni",42,100000,7)
