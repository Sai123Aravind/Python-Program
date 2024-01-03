rows=int(input("Enter a rows ="))
col=int(input("Enter a column ="))
for var1 in range(rows):
    for var2 in range(col):
        if var1==0 or var1==rows-1:
            print("+",end=" ")
        else:
            if var2==0 or var2==col-1 or var2==var1 or rows-var1-1==var2:
                print("+",end=" ")
            else:

            
                print(' ',end=" ")
    print()