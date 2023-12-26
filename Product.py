#Product of numbers in list
sum=0
product=0
a=[1,9,11,23,65,78,43]

   
if len(a)%2==0:
     for var in a:
        sum=sum+var
     print(sum)
else:
     for var in a:
        product=product*var
print(product)
     