flag=""
a=0
i=1
while(a<3):

    j=1
    if flag:
        i=j*i+5
    else:
        i=j*i+1
    a=a+1
print(i)
