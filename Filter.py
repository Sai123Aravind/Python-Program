def even(a):
    if a%2==0:
        return True
    else:
        return False
b=filter(even,[1,2,3,4,5,6,7,8,9])
print(list(b))