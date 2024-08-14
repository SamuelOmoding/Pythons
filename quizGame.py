# Python quiz game

questions = ("How many elements are in the periodic table?: ",
             "What is the capital of Kenya?: ",
             "Who invented the telephone?: ",
             "Which country in Africa is the best in athletics?: ",
             "What is the chemical symbol for gold?: ")

options = (("A. 117","B. 119", "C. 116", "D. 118", "E. 120"), 
           ("A. Mombasa","B. Kisumu", "C. Nairobi", "D. Nakuru", "E. Kampala"), 
           ("A. Graham Bell","B. Newton", "C. Lincorn", "D. Alexander the Great", "E. The Wright Brothers"), 
           ("A. Ethiopia","B. Kenya", "C. Uganda", "D. Egypt", "E. Botswana"), 
           ("A. Ca","B. K", "C. Au", "D. Na", "E. Cu"))

answers = ("D", "C", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("...................")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D, E): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")  
        print(f"{answers[question_num]} is the correct answer")      
    question_num += 1  
    
print("...................")
print("      RESULTS      ")
print("...................")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: ", round(score, 0), "%")



    
      