# print('Welcome to the store')

# options = input('Shall we proceed or not? ').strip().lower()

# if options == "proceed":
#     print('Please login')
#     name = input('Enter your name: ').strip() 

#     if name: 
#         print(f"Hi, {name}!")
#     else:
#         print("You didn't enter a name.")
# else:
#     print("Okay, see you next time!")
# i=1
# while i<=5:
#     print('hello')
#     choice=input('enter your choice y/n ?')
#     i=i+1
#     if choice=='y':
#         continue
#     else:
#         break
# else:
#         print('program completed successfullyy')
print("**Union Bank Of India Welcomes, You**")
current_balance = 2000
categories = input('choose your options 1.Deposit 2.Withdraw 3.Checkbalance').strip().lower()
if categories== 'deposit':
    amount = int(input("please enter your amount in numbers"))
    print(f"your amount of rupees {amount} deposited into your account, your current balance ={amount+current_balance}")

if categories == 'withdraw':
    debit=int(input('please enter amount '))
    print(f"your amount of rupees {debit} was debited from your account, your total balance ={current_balance-debit}")
if categories=="checkbalance":
    balance = input('please enter your pin ')
    if balance=='1234':
        print(f'your current balance is{current_balance}')
    else:
        print(" Incorrect PIN.")



