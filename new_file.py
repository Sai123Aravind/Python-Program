file=open("File creation.txt","w")
data="Hello to Every one"
file.write(data)
file.close()

file=open("File creation.txt","r")
data=file.read()
file.close()
print(data)

file=open("File creation.txt","a")
data=[
    "balaji\n"
    "Gangadhar\n"
    "Varalakshmi\n"
    "Eshwra\n"
]
file.writelines(data)
file.close

file=open(r"path","r")
data=file.read()
file.close()
print(data)