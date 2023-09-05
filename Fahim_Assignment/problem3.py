# 3. Conditions – If, Else, Elif:
# Write a program that asks the user for a number and prints whether the number is even or odd.

number= int(input("Enter a number: "))
if number % 2 == 0:
        print(f"{number} is even.")
else:
        print(f"{number} is odd.")
