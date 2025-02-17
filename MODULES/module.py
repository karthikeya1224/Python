import random as r
score=0
for i in range(1,6):
    num1=r.randint(1,10)
    num2=r.randint(1,10)
    result=num1+num2
    print(f"{i}.{num1}+{num2}=")
    answer=int(input("enter your answer:"))
    if answer==result:
        score+=1
print(f"your score={score}")
