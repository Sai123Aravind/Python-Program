import random
otp=''
while len(otp)<4:
    otp=otp+str(random.randint(0,9))
print(otp)