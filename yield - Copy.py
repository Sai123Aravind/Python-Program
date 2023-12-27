def cal(a,b):
    for var in range(a,b+1):
        
         yield var**2
         yield var*2
c=cal(5,15)
print(c)
