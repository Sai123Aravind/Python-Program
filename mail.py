a=input('enter a user')
i=0
out=0
while i<len(a):
    if'0'<=a[i]<='9':
        out=out+a[i]
    i=i+1
print(out)
