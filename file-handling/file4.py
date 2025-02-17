import os
os.chdir("E:/karPy")
print("**FILE MANAGER**")
while True:
    print("1.WRITE")
    print("2.READ")
    print("3.REMOVE")
    print("4.EXIT")
    choice=input("enter your choice: ")
    if choice=="1":
        f=open("myfile.txt","a")
        data=input("enter data: ")
        f.write(data)
        f.close()
    elif choice=="2":
        f=open("myfile.txt","r")
        data=f.read()
        print(data)
        f.close()
    elif choice=="3":
       os.remove("myfile.txt")
    elif choice=="4":
        break


