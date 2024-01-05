import re
email="saiaravind22@gmail.com"
out=re.findall('[a-z]+[1-9]*\@gmail\.com',email)
print(out)