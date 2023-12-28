a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
out=[]
for var,var1,var2 in zip(a,b,c):
    out=out+[var]+[var1]+[var2]
print(out)

 