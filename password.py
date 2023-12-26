# Printing of a Password with some rules
password=eval(input("enter a the password:-"))
Validate={'upper':0,'lower':0,'number':0,'special':0}
if len(password)>=8:
    for var in password:
        if(var<='A' and var<='Z'):
            Validate['upper']=Validate['upper']+1
        elif(var<='a' and var<='z'):
            Validate['lower']=Validate['lower']+1
        elif(var<='0' and var<='9'):
            Validate['number']=Validate['number']+1
        elif(var!=''):
            Validate['special']=Validate['special']+1
    if( Validate['upper'] and Validate['lower'] and Validate['number'] and Validate['special']):
      print("It is valid password")
    else:
      print("It is a invalid passsword")
