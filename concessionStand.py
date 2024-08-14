# Concession stand program
# Understanding how to work with dictionaries{"a collection of key-value pairs i.e item and price"}
# dictionary {key:value}
menu = {"pizza": 800,
        "burger": 500,
        "fries": 300,
        "soda": 250,
        "water": 250,
        "cookies": 200,
        "lemonade": 250,
        "nachos": 250,
        "popcorn": 650}
cart = []
total = 0

print("........MENU........")
for key, value in menu.items():
    print(f"{key.capitalize():10}: Ksh.{value:.2f}")
print("........MENU.........")

while True:
    food = input("Enter an item to add to the cart (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not on the menu. Please choose an item from the menu.")

print("........YOUR ORDER.........")        
for food in cart:
    total += menu.get(food)
    print(food.capitalize())       

print()
print(f"Total is: Ksh.{round(total, 2)}")
