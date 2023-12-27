def upper(a):
    if a>'A' and a<'Z':
        return True
    else:
        return False
out=filter(upper,"aBc@15$67DEfgh")
print(list(out))