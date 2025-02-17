import os 
os.chdir("E:/karPy")
f=open("myfile.txt","w")
try:
    f.write('hello world')
    print ("writing to the file")
except IOError:
    print("could not write into file.")
else:
    print("successfully wrote")
finally:
    f.close()
    print('file closed successfully')