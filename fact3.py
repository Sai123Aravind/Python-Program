#factorial
def fact(a):
    fact=1
    i=1
    while(i<=a):
        fact=fact*i
        i=i+1
    return fact
    
b=fact(6)
print(b)