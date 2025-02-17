import os
os.chdir("E:/karPy")
with open("myfile.txt","r") as file:
    data=file.read()
    print(data)
