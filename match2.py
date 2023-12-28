print("Enter a colour blw RED,YELLOW,GREEN")
option=input("Enter a colour")
match option:
    case'Green':
        print("go")
    case 'Yellow':
        print("Ready to go")
    case 'Red':
        print("stop")
    case _:
        print("Invalid")
