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
    
    print("*****************************************")      
    print(f"Game over! Your balance is KES.{balance}")
    print("*****************************************")      


if __name__ == "__main__":
    main()