str="the date is 04/01/2024"
out=0
for var in str:
    if '0'<=var<='9':
        out=out+int(var)
print(out)
