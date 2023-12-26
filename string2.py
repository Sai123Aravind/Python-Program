#Finding frequency
def string(a,b):
    count=0
    for var in a:
         if var==b:
          count=count+1
    return count

c=string('aravind','a')
print(c)