#Reversing of String
char=eval(input("Enter a String"))
i=0
char1=''
while(i<len(char)):
    char1=char[i]+char1
    i=i+1
print(char1)