#Finding index number and storing it in a varible by using while
def Index(a):
    b=[]
    i=0
    while(i<len(a)):
        if a[i] in 'aeiouAEIOU':
            b=b+[i]
            
        i=i+1
    return b
c=Index("happy new year")
print(c)