user={'Username':'Aravind','Password':123456}
Username=eval(input("Enter ur User name :"))
Password=eval(input("Enter ur Password :"))
if Username==user['Username']:
    print('the user name is vaild')
else:
    print('the user name is invaild')
if Password==user['Password']:
    print('The password is valid')
else:
    print('the password is invaild')