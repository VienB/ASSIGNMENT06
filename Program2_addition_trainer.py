# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

import random

score = 0
question = 0

print("WELCOME! LET'S TEST YOUR ADDING SKILLS.\n")

Fnumber = random.randint(0,99)
Snumber = random.randint(0,99)
operation = ("+")
answer = Fnumber + Snumber
print((Fnumber), "+" ,(Snumber), "= ??")