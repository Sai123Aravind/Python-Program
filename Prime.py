#Prime number
num=int(input("Enter a number"))
i=1
temp=False
while(i<=num):
    if num%i==0 and i!=1 and i!=num:
        temp=True
    i=i+1
if not temp:
    print("It is prime")
else:
    print("Its is not prime")