number = int(input("Enter a number: "))

if number % 2 == 0 and number % 5 == 0:
    print("This number is divisible by 2 and 5.")
elif number % 2 == 0:
    print("{number} is even")
else:
    print("{number} is odd")


