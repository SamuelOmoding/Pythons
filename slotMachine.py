# Python slot machine

import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '🟊']
    
    return [random.choice(symbols) for _ in range(3)]
    # results = []
    # for symbols in range(3):
    #     results.append(random.choice(symbols))
    # return results        

def print_row(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🟊':
            return bet * 20
    return 0    
    

def main():
    balance = 100
    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 🟊 ")
    print("***********************")
    
    while balance > 0:
        print(f"Current Balance: KES.{balance}")
        
        bet = input("Place your bet amount: ")
                
        if not bet.isdigit():
            print("Please enter a positive numeric value.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds!")
            continue
        
        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue
        
        balance -= bet
        
       
        payout = get_payout(row,bet)
        
        if payout > 0:
            balance += payout
            print(f"Congratulations! You won KES.{payout}")
        else:
            print("Sorry, you lost your bet.")
            
        play_again = input("Do you want to spin again? (Y/N): ") 
        
        if play_again.lower()!= "y":
            break   
    print("*****************************************")      
    print(f"Game over! Your balance is KES.{balance}")
    print("*****************************************")      


if __name__ == "__main__":
    main()