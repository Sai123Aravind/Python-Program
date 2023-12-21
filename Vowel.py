# to find the vowels
a=(input('Enter a Character:'))
if type(a)==str:
    if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
        print('Given Character is Vowel')
    else:
        print('No')
else:
    print('given is Not a Character')
       
