#Define the menu of restaurant in a hotel
menu={'Pasta':250,
      'Pizza':500,
      'Burger':150,
      'Salad':100,
      'Soup':120,
      'Steak':800,
      'Sandwich':200,
      'Dessert':300}

#Greet 
print("Welcome to our Hotel Restaurant!")
print("Here is our menu:")
#Display the menu
print("Pizza:500\nPasta:250\nBurger:150\nSalad:100\nSoup:120\nSteak:800\nSandwich:200\nDessert:300")
#Take order from the customer
order_total=0
item_1=input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total+=menu[item_1]
else:
    print(f"Sorry, we don't have {item_1} on the menu.")    

another_order=input(f"do you want to order anything else? (yes/no)")
if another_order.lower()=='yes':
    item_2=input("Enter the second item you want to order: ")
    if item_2 in menu:
        order_total+=menu[item_2]
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")

print(f"Your total order amount is: {order_total} INR")