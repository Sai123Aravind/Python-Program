a=eval(input("enter a number with 0&1"))
i=0
num=''
while(i<len(a)):
    if (a[i]=='1'):
        num=num+'0'
    else:
        num=num+'1'
    i=i+1
print(num)