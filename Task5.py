class Cart:
    quantity={'T.V':10,'Mobile':20,'laptop':5}
    price={'T.V':10000,'Mobile':5000,'laptop':20000}
    def __init__(self,name,mobile,location,total_quantity,total_price):
        self.name=name
        self.mobile=mobile
        self.location=location
        self.total_quantity=total_quantity
        self.total_price=total_price
    @classmethod   
    def Book(self,product,total_quantity,total_price):
        print("Please enter that u need book 1. TV,2. Mobile,3. laptop ")
        self.product=input("select the product")
        if (product=="TV"):
            print("u have selcted tv and the cost is 10000")
        elif(product=="Mobile"):
            print("U have selected mobile and the price is 5000")
        elif(product=="Laptop"):
            print("U have selected laptop and the price is 20000")
        self.total_quantity=input("select the quantity")

    def generate_slip():
        pass
    def get_details():
        pass

     