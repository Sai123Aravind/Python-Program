import re
st="The date 9 data is 04/01/2024"
data=re.findall('\d',st)
print(data)