# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")
# ask user input
uno = int(input("ENTER FIRST NUMBER: "))
dos = int(input("ENTER SECOND NUMBER: "))
tres = int(input("ENTER THIRD NUMBER: "))
quatro = int(input("ENTER FOURTH NUMBER: "))

if uno > dos and uno > tres and uno > quatro:
    highest = uno

else:
    if dos > quatro:
        highest = dos

    else:
        if tres > quatro:
            highest = tres

        else:
            highest = quatro

print(f"The order of four numbers is: {uno}, {dos}, {tres}, {quatro}.")