import re
num='+91-6789548787'
data=re.findall('\+91-[6789][0-9]{9}',num)
print(data)