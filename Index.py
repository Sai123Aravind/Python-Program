#finding index number and storimg it in a variable using for loop
def Index(a):
    b=[]
    for var in range(0,len(a)):
       if a[var] in'a,e,i,o,u,A,E,I,O,U':
           b=b+[var]
    return b
c=Index('aravind')
print(c)

 