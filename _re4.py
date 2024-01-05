import re
st='AP40ER4567 '
data=re.findall('AP[0-4]\d[A-Z]{2}\d{4}',st)
print(data)