print("***CALCULATOR***")
print("**1.ADDITION** **2.SUBTRACTION** **3.MULTIPLICATION** **4.DIVISION** **5.MODULO DIVISION**")
operators = int(input("Choose your option from above (Enter the number): "))
def calci():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    return n1, n2
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def mod(n1, n2):
    return n1 % n2
n1, n2 = calci()
if operators == 1:
    print(f"Result: {add(n1, n2)}")
elif operators == 2:
    print(f"Result: {sub(n1, n2)}")
elif operators == 3:
    print(f"Result: {mul(n1, n2)}")
elif operators == 4:
    print(f"Result: {div(n1, n2)}")
elif operators == 5:
    print(f"Result: {mod(n1, n2)}")
else:
    print("Invalid option! Please choose a number between 1 and 5")


