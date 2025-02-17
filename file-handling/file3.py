import os
os.chdir("E:/karPy")
f=open("myfile.txt","w")
while True:
    name=input("enter name: ").strip().upper()
    age=int(input('enter age: ').strip())
    phno=int(input("enter phno: ").strip())
    f.write(f"{name},{age},{phno}")
    next=input("do you want to continue..?")
    if next=="yes":
        continue
    elif next=="no":
        break

f.close()