# Hangman in Python
from wordslist import words                 
import random


# Dictionary for hangman art
hangman_art = {
    0: (" ", " ", " "),
    1: (" o ", " ", " "),
    2: (" o ", " | ", " "),
    3: (" o ", "/|", " "),
    4: (" o ", "/|\\", " "),
    5: (" o ", "/|\\", "/ "),
    6: (" o ", "/|\\", "/ \\")
}


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)  # Initialize hint as a list of underscores
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You've guessed the word correctly.")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Sorry, you've lost. The word was:", answer)
            is_running = False    

if __name__ == "__main__":
    main()
