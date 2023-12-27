def even(a):
    if a%2==0:
        return a**2
    else:
        return a**3
out=map(even,[2,4,6,8])
print(list(out))