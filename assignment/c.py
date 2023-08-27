# Conditions – If, Else, Elif:
# Write a program that asks the user for a number and prints whether the number is even or odd.

def check(num):
    if num&1:
        print("Number is odd")
    else : 
        print("Number is even")

num=int(input("Enter a number : "))

check(num)