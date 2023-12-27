def fact(var,i=1):
    
    if(i==var):
        return i
    return i*fact(var,i+1)
out=fact(5)
print(out)

    
