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
