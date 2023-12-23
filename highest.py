a=[1,9,11,23,-65,-78,43]
highest=a[0]
highest2=a[0]
for var in a:
    if highest<var:
        highest=var
for var in a:
    if highest2<var and var!=highest:
        highest2=var
   
print(highest)
print(highest2)
