#Adding the sum of the numbers in the list
def list(a):
    num=0
    for var in a:
        if type(var)==int:
            num=num+var
    print(num)
list([1,2,'str',3,44])