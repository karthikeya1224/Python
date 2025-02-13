#  for i in range(5):
#     print(i)
# for i in range(13,1):
#     print(f'2*{i}={i*2}')
# for j in range(1,4):
#     for i in range(1,13):
#         print(f"{j} x {i}={j*i}")
# j=2
# while j<=5:
#     i=1
#     while i<=13:
#         print(f"{j}x{i}={j*i}")
#         i+=1
#     j+=1

# for i in range(0,5):
#     print("*"*5 ,end=" ")
# for j in range(0,6):
#     for i in range(6):
#         print(j,end=" ")
#     print()
   
# for j in range(1,6):
#     for i in range(6):
#         print(i,end=' ')
#     print()
# for j in range(1,7):
#     for i in range(1,j):
#         print(i,end=" ")
#     print()/
# for j in range(1,7):
#     for i in range(1,j):
#         print("*",end=" ")
#     print()
# for j in range(5,0,-1):
#     for i in range(j):
#            print("*",end=" ")
#     print()
# i=1
# while i<=25:
#     print(i)
#     i=i+5

# for i in range(1,30,5):
#  print(i)

# ame=input("shall we proceed or not?")
# if ame=="yes":
#     me=input("enter name")
#     print(f'{me}.append()')
# ame = input("Shall we proceed or not? ").strip().lower()
# if ame == "yes":
#     me = [] 
#     name = input("Enter name: ")  
#     me.append(name) 
#     print(f"Updated list of names: {me}") 
# ame = input("Shall we proceed or not? ").strip().lower()  # Normalize input

# if ame == "yes":
#     me = []  # Initialize an empty list to store names
#     while True:  # Infinite loop to keep asking for names
#         name = input("Enter name (or type 'stop' to exit): ").strip()
#         if name.lower() == "stop":  # Condition to break the loop
#             break
#         me.append(name)  # Append the entered name to the list
#         print(f"Updated list of names: {me}")  # Print the updated list after each input

# print("Final list of names:", me)
inpt=input('shall we proceed or not..?').strip().lower()
if inpt=="yes":
     names=[]
while True:
    name=input('enter name: or stop or exit ')
    if name.lower().strip()=="stop":
        break
    names.append(name)
    print(names)

