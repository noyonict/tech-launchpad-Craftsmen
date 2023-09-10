# 3. Conditions – If, Else, Elif:

# Write a program that asks the user for a number and 
# prints whether the number is even or odd.

number = int(input("Enter a number: "))
remainder = number % 2

if remainder == 0:
    print("This is an Even number")
else:
    print("This is an Odd number")

