st='1 6 567 The 92 data is 04/01/2024'
out=''
for var in st:
    if '0'<=var<='9':
        out=out+var
print(list(out))