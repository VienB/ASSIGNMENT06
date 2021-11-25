# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")
# ask user input
uno = int(input("ENTER FIRST NUMBER: "))
dos = int(input("ENTER SECOND NUMBER: "))
tres = int(input("ENTER THIRD NUMBER: "))
quatro = int(input("ENTER FOURTH NUMBER: "))

if uno >= dos and uno >= tres and uno >= quatro:
    # 1,2,2,3,3,4
    if uno >= dos and dos >= tres and tres >= quatro:
        print(f"The arrangement of the numbers is: {uno}, {dos}, {tres}, {quatro}.")
    # 1,2,2,4,4,3
    elif uno >= dos and dos >= quatro and quatro >= tres:
        print(f"The arrangement of the numbers is: {uno}, {dos}, {quatro}, {tres}.")
    # 1,3,3,4,4,2
    elif uno >= tres and tres >= quatro and quatro >= dos:
        print(f"The arrangement of the numbers is: {uno}, {tres}, {quatro}, {dos}.")
    # 1,3,3,2,2,4
    elif uno >= tres and tres >= dos and dos >= quatro:
        print(f"The arrangement of the numbers is: {uno}, {tres}, {dos}, {quatro}.")
    # 1,4,4,2,2,3
    elif uno >= quatro and quatro >= dos and dos >= tres:
        print(f"The arrangement of the numbers is: {uno}, {quatro}, {dos}, {tres}.")

    else:
        print(f"The arrangement of the numbers is: {tres}, {dos}, {quatro}, {uno}.")

elif dos >= uno and dos >= tres and dos >= quatro:
    # 2,1,1,3,3,4
    if dos >= uno and uno >= tres and tres >= quatro:
        print(f"The arrangement of the numbers is: {dos}, {uno}, {tres}, {quatro}.")
    # 2,1,1,4,4,3
    elif dos >= uno and uno >= quatro and quatro >= tres:
        print(f"The arrangement of the numbers is: {dos}, {uno}, {quatro}, {tres}.")
    # 2,3,3,4,4,1
    elif dos >= tres and tres >= quatro and quatro >= uno:
        print(f"The arrangement of the numbers is: {dos}, {tres}, {quatro}, {uno}.")
    # 2,3,3,1,1,4
    elif dos >= tres and tres >= uno and uno >= quatro:
        print(f"The arrangement of the numbers is: {dos}, {tres}, {uno}, {quatro}.")
    # 2,4,4,1,1,3
    elif dos >= quatro and quatro >= uno and uno >= tres:
        print(f"The arrangement of the numbers is: {dos}, {quatro}, {uno}, {tres}.")

    else:
        print(f"The arrangement of the numbers is: {tres}, {uno}, {quatro}, {dos}.")

elif tres >= uno and tres >= dos and tres >= quatro:
    # 3,1,1,2,2,4
    if tres >= uno and uno >= dos and dos >= quatro:
        print(f"The arrangement of the numbers is: {tres}, {uno}, {dos}, {quatro}.")
    # 3,1,1,4,4,2
    elif tres >= uno and uno >= quatro and quatro >= dos:
        print(f"The arrangement of the numbers is: {tres}, {uno}, {quatro}, {dos}.")
    # 3,2,2,4,4,1
    elif tres >= dos and dos >= quatro and quatro >= uno:
        print(f"The arrangement of the numbers is: {tres}, {dos}, {quatro}, {uno}.")
    # 3,2,2,1,1,4
    elif tres >= dos and dos >= uno and uno >= quatro:
        print(f"The arrangement of the numbers is: {tres}, {dos}, {uno}, {quatro}.")
    # 3,4,4,1,1,2
    elif tres >= quatro and quatro >= uno and uno >= dos:
        print(f"The arrangement of the numbers is: {tres}, {quatro}, {uno}, {dos}.")

    else:
        print(f"The arrangement of the numbers is: {dos}, {uno}, {quatro}, {tres}.")

elif quatro >= uno and quatro >= dos and quatro >= tres:
    # 4,1,1,3,3,2
    if quatro >= uno and uno >= tres and tres >= dos:
        print(f"The arrangement of the numbers is: {quatro}, {uno}, {tres}, {dos}.")
    # 4,1,1,2,2,3
    elif quatro >= uno and uno >= dos and dos >= tres:
        print(f"The arrangement of the numbers is: {quatro}, {uno}, {dos}, {tres}.")
    # 4,3,3,2,2,1
    elif quatro >= tres and tres >= dos and dos >= uno:
        print(f"The arrangement of the numbers is: {quatro}, {tres}, {dos}, {uno}.")
    # 4,3,3,1,1,2
    elif quatro >= tres and tres >= uno and uno >= dos:
        print(f"The arrangement of the numbers is: {quatro}, {tres}, {uno}, {dos}.")
    # 4,2,2,1,1,3
    elif quatro >= dos and dos >= uno and uno >= tres:
        print(f"The arrangement of the numbers is: {quatro}, {dos}, {uno}, {tres}.")

    else:
        print(f"The arrangement of the numbers is: {tres}, {uno}, {dos}, {quatro}.")


