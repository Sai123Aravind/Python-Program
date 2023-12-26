#finding length of using return kw
b=[1,2,3]
def length(a):
    count=0
    for var in a:
        count=count+1
    print(count)
    return count
c=length(b)
print(c)