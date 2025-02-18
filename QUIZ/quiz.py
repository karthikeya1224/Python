import random as r

score = 0  

for i in range(1, 6):  
    opp = ["+", "-", "*", "%"]
    num1 = r.randint(1, 10)
    num2 = r.randint(1, 10)
    operators = r.choice(opp)
    if operators == "+":  
        result = num1 + num2  
    elif operators == "-":  
        result = num1 - num2  
    elif operators == "*":  
        result = num1 * num2  
    elif operators == "%":  
        result = num1 % num2  
    print(f"{i}. {num1} {operators} {num2} = ?")  
    try:  
        answer = int(input("Enter answer: "))  
        if answer == result:  
            score += 1 
    except ValueError:  
        print("WRONG ANSWER")  
print(f"Your final score is: {score}/5")   

