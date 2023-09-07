# Q3: Write a program that asks the user for a number and prints whether the number is even or odd.
number = int(input("Input your number: ").strip())


if number%2 == 0:
    print("Your number is 'EVEN'")
else:
    print("Your number is 'ODD'")


