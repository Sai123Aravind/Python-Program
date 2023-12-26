#Finding no.of vowels , consonets,and special charcters i String
a=eval(input("Enter a String"))
vowel_count=0
consonent_count=0
Special_count=0
for i in a:
    if(i in 'a,e,i,o,u,A,E,I,O,U'):
        vowel_count+=1
    elif(i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
        consonent_count+=1

    else:
        Special_count+=1
print(vowel_count)
print(consonent_count)
print(Special_count)