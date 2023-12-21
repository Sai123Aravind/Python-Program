char=eval(input("Enter ur mail"))
i=0
num=''
while(i<len(char)):
    if('0'<=char[i]<='9'):
        num=num+char[i]
    i=i+1
print(num)

