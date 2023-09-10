# 10. Final Challenge – Comprehensive:

# Create a program that does the following:
# Defines a function is_prime which checks if a number is prime.
# Prompts the user to enter a range (two numbers).
# Uses a loop to go through the numbers in the given range.
# Prints out all prime numbers in that range.


def is_prime(number_arg):
    prime = True
    for checker_number in range(2, number_arg):
        if checker_number * checker_number > number_arg:
            break

        if number_arg % checker_number == 0:
            prime = False
            break

    return prime


numbers = input("Enter two numbers separated by space: ")
numbers = numbers.split()

if int(numbers[0]) > int(numbers[1]):
    smaller = numbers[1]
    greater = numbers[0]
else:
    smaller = numbers[0]
    greater = numbers[1]

for number in range(int(smaller), int(greater) + 1):
    if is_prime(number):
        print(number)

