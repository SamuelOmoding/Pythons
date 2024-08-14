# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: Ksh."))
        foods.append(food)
        prices.append(price)
        
print("...... YOUR CART ......")  

for food in foods:
    print(f"{food}: Ksh.{prices[foods.index(food)]:.2f}")

for price in prices:
    total += price
print()    
print(f"Your total is: Ksh.{total:.2f}")  