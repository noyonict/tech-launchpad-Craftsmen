num = int(input("Enter number: "))


if num % 2 == 0 and num % 5 == 0:
    print(f"This number, {num} is divisible by 2 and 5.")
elif num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number, {num} is ODD")