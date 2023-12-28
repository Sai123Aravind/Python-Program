a=int(input("Enter a number ="))
b=int(input("Enter a number ="))
c=eval(input("Enter a Symbol for arthmetic operation ="))
result=0
match c:
    case'+':
        result=a+b
    case'-':
        result=a-b
    case'*':
        result=a*b
    case'/':
        result=a/b
    case _:
        result=None
print(result)
