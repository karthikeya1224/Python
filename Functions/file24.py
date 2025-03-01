# num1 = int(input("Enter a number: "))  
# num2 = int(input("Enter another number: "))  
# result = num1 / num2  
# print("Result:", result)
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Please enter a valid number!")
# try:
#     x = 10 / 0 
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except Exception as e:
    print(f"An error occurred: {e}")


