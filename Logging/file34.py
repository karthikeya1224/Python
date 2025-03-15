import logging
logging.basicConfig(filename='bank.log',level=logging.INFO)
balance=0
for i in range(3):
    amount=int(input("enter amount:"))
    logging.info(f'{amount}was credited')
    balance+=amount
    logging.info(f"current balance is {balance}")
    print(balance)