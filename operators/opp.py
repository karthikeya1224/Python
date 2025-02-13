availableBalance = 2000
price =300
quantity = 6
total_price= price * quantity
print(f"Total Price ={total_price}")
can_afford = total_price <= availableBalance 
print(f"can afford : {can_afford}")
discount = 150
discount_applicable = (quantity>=4) and (availableBalance>total_price)
print(f"applicable discount = {discount_applicable}")
if discount_applicable :
    total_price -= discount
    print(f"total price after discount= {total_price}")
    fruits = ['apple','banana','mango']
    item_to_check='banana'
    is_item_in_cart= item_to_check in fruits
    print(f"{item_to_check} is there in the cart so it is {is_item_in_cart}")