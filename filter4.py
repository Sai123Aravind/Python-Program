#Can't do any operation in Filter 
def double(a):
    return a*2
out=filter(double,[1,2,3,4])
print(list(out))