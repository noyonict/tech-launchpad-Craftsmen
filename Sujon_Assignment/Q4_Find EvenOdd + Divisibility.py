number = int(input("Enter the number you want to check: "))

if number % 2 == 0:
    print(f"{number} is an Even Number")
else:
    print(f"{number} is an Odd Number")


if number % 2 == 0 and number % 5 == 0:
    print("This number is divisible by 2 and 5.")

elif number % 2 == 0:
    print("This number is divisible by 2 not by 5.")

elif number % 5 == 0:
    print("This number is divisible by 5 not by 2.")

else:
    print("This number is not divisible by both 2 and 5.")
