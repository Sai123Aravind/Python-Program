num=eval(input("enter a number"))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("It is perfect number")
else:
    print("It is not perfect number")
