# printing capcha
import random
capcha=''
while len(capcha)<6:
    capcha=capcha+chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(0,9))
print(capcha)
    