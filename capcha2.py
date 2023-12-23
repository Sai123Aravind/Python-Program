import random
out=[]
capcha=''
while len(out)<6:
    out=out+[chr(random.randint(65,90))]
    out=out+[chr(random.randint(97,122))]
    out=out+[str(random.randint(0,9))]
    random.shuffle(out)
    for var in out:
        capcha=capcha+var
print(capcha)