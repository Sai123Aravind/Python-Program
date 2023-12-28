seats=int(input("enter the seats"))
option=int(input("select the option"))
match option:
    case 1:
        print("diamond ")
        amt=seats*200
    case 2:
        print("Gold")
        amt=seats*150
    case 3:
        print("Silver")
        amt=seats*100
    case __:
        amt=None
print(amt)
