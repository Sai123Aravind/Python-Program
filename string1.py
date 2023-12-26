# to count numbers in string
def string():
    char=eval(input("Enter a string"))
    count=0
    for var in char:
        if var>='0' and var<='9':
            count=count+1

    print(count)
string()