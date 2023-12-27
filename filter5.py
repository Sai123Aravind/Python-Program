def lower(a):
    if a>'a' and a<'z':
        return True
    else:
        return False
def ord(a):
    return ord(a)
out=map(ord,(filter,(lower,"a1b2C3Def12@#9Z")))
print(list(out))