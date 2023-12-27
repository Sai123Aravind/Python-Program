def sample(a):
        for var in range(0,len(a)):
            if(a[var] in 'aeiouAEIOU'):
                yield a[var]
                yield [var]
c=sample("god father anil")
print(c)
