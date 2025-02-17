import sys
sys.path.append("./QUIZ") 
sys.path.append("./CALCI") 

from QUIZ import quiz
from CALCI import calculator

print("1. QUIZ")
print("2. CALCULATOR")

try:
    project = int(input("Enter your choice (1 or 2): "))

    if project == 1:
        quiz.quiz() 
    elif project == 2:
        calculator.calculator()
    else:
        print("Invalid option! Please enter 1 or 2.")

except ValueError:
    print("Invalid input! Please enter a number.")

