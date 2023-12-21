# To know the percentage of Student
marks=(eval(input("Enter the marks u gained :")))
if(marks>90 and marks<=100):
    print("your grade is A+")
elif(marks>80 and marks<=90):
    print("Your grade is A")
elif(marks>70 and marks<=80):
    print("Your grade is B")
elif(marks>=60 and marks<=70):
    print("your grade is C")
elif(marks>=30 and marks<60):
    print("your pass")
elif(marks>=0 and marks<30):
    print("fail")
else:
    print("Enter a vaild marks")