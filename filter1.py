def data(a):
    if type(a) in (int,float,complex,bool):
        return True
    else:
        return False
out=filter(data,[1,2,(112,13),[1,2,3],4,5,6])
print(list(out))