def add(var,i=0):
    if len(var)-1==i:
          return var[i]
    return var[i]+add(var,i+1)
c=add([4,7,6,2])
print(c)

