import re
st='RTRTR2541H'
data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
print(data)