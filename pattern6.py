row=int(input("Enter a row ="))
out='''
'''
for var in range(1,row+1):
    out=out+("  "*(row-var)+"* "*var)
    out=out+'\n'
for var in range(0,row):
    out=out+("  "*(row-var)+"*"*(var*2+1))
    out=out+'\n'
name=input("Enter a name")
with open(f'{name}.txt','w') as file:
    file.write(out)