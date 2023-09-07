number = int(input("Enter a number: "))

if number % 2 == 0 and number % 5 == 0:
    print("This number is divisible by 2 and 5.")
elif number % 2 == 0:
    print("This number is only divisible by 2.")
elif number % 5 == 0:
    print("This number is only divisible by 5.")
else:
    print("This number is not divisible by 2 or 5.")
