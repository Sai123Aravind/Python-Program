#Finding no.of vowels
char=eval(input("enter a string"))
i=0
count=0
while(i<len(char)):
    if(char[i] in "a,e,i,o,u,A,E,I,O,U"):
        count+=1
    i=i+1
print(count)