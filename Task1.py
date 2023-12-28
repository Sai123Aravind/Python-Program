print("Welcome to Book my Show")
name=((input("Enter ur name =")))
seats=(eval(input("Enter no.of seats u need to book =")))
print("Enter 1 to select Diamond class")
print("Enter 2 to select Gold class")
print("Enter 3 to select Silver class")
type=(int(input("Enter the Type of seat u required =")))

if(type==1):
    print("U have selected diamond class and the rate is 200")
    cost=200
elif(type==2):
    print("U have selected glod class and the rate is 150")
    cost=150
elif(type==3):
    print("U have selected silver class and the rate is 100")
    cost=100
else:
    print("Invalide seat")
print("your name is ",name)
print("you have booked ",seats,"seats")
print("you have selected type ",type,"and the amount is",seats*cost)