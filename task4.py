a="ABCDEFGIJKABC"
out=''
i=0
while(i<len(a)):
    if(a[i]!=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]):
        out=out+a[i]
        break 
        
    i=i+1
print(out)