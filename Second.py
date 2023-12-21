# to find Second Higest number
num1=eval(input("Enter a num1 :"))
num2=eval(input("Enter a num2 :"))
num3=eval(input("Enter a num3 :"))
if(num1>num2 and num1>num3):
    if(num2>num3):
        print(num2, "is the  second greatest")
    else:
        print(num3, "is the second greatest")
elif(num2>num3):
    if(num1>num3):
        print(num1,"is the second greatest")
    else:
        print(num3,"is the  second greatest")
else:
    if(num1>num2):
        print(num1, "is second greatest")
    else:
        print(num2 ,"is the second greatest")
