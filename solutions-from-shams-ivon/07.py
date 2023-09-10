# 7. While Loop & Condition:

# Implement a program where the user is repeatedly asked to enter numbers 
# until they type 'stop'. Once they do, the program should display the sum of all the numbers entered.


sum_of_numbers = 0

while True:
    number = input("Enter a number: ")
    if number == "stop":
        break

    if not number.isdigit():
        print("This is neither a number nor a 'stop' command!")
        continue

    sum_of_numbers = sum_of_numbers + int(number)

print(sum_of_numbers)
