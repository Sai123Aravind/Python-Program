result=[]
for vr in range(1,10):
    fact=1
    for var in range(1,vr+1):
        fact=fact*var
        result=result+fact
print(result)