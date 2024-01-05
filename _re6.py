import re
file=open(r"C:\Users\administrator.MCA\Desktop\content.txt",'r+')
data=file.read()
data1=re.sub('a','@',data)
file.write(data1)