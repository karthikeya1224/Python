# file = open("example.txt", "w")  # Opens file in write mode
# file.write("Hello, this is a test file.")  # Writing content
# file.close()  # Always close the file after writing
# with open("data.txt", "a") as file:
#     file.write("\nAppending more content!")  
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
# with open("data.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())  # Remove newline characters
# with open("data.txt", "r") as file:
#     print(file.readline())  # Reads the first line only
import os
# os.chdir('E:/')
# os.mkdir('karPy')
os.chdir('E:/karPy')
f=open("myfile.txt","a")
f.write('\nthis is a second  file')
f.close()



