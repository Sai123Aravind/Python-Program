
a=input('enter a user')
i=0
out=0
while i<len(a):
    if type(a)==int:
        out=out+a[i]
    i=i+1
print(out)
