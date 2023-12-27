def odd(a):
    if (a%2==1):
        return a,a**2
    else:
        return False
out=map(odd,range(1,100))
print(list(out))