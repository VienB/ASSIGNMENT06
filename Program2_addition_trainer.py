# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

import random

print("WELCOME! LET'S TEST YOUR ADDING SKILLS.\n")
AdditionQuiz = 0
score = 0

while AdditionQuiz != 10:
    AdditionQuiz = AdditionQuiz + 1
    Fnumber = int(random.randint(0,99))
    Snumber = int(random.randint(0,99))
    print(f"\n{Fnumber} + {Snumber} = ??", end = " ")
    YourAnswer = int(input("\nENTER YOUR ANSWER: "))
    answer = Fnumber + Snumber

    if answer == YourAnswer:
        print("CONGRATS! YOU ARE CORRECT")
        score = score + 1
    else:
        print("ENGKK! THE CORRECT ANSWER IS:", answer)
        score = score + 0

print("\nYOUR TOTAL SCORE IS: " + str(score) + "/10")