import re
file=open(r"C:\Users\administrator.MCA\Desktop\content.txt",'r')
data=file.read()
data1=re.split(' ',data)
count=0
words=[]
for var in data1:
    out=re.match('^a',var)
    if out:
        words+=[var]
        count=count+1
print(count)
print(words)