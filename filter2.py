def multiple(a):
    if a%5==0 and a%3==0:
        return True
    else:
        return False
out=filter(multiple,range(1,201))
print(list(out))