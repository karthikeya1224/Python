# import re
# var="Karthikeyakadali2000@gmail.com"
# ser="2000"
# flag=re.search(ser,var)
# if flag:
#     print("valid")
# else:
#     print("invalid")
# import re
# name="234424242131"
# pattern="[0-9]"
# flag=re.search(pattern,name)
# if flag:
#     print("valid")
# else:
#     print("invalid")
import re
# str='hi how are you'
# pattern="^hi.*you$"
# flag=re.search(pattern,str)
# if flag:
#     print("valid")
# else:
#     print("invalid")
str="abc@gmail.com pqr@gmail.com xyz@gmail.com"
pattern = " "
result=re.split(pattern,str)
print(result)