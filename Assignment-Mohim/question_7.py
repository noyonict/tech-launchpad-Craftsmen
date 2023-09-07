total_sum = 0

while True:
    user_input = input("Enter a number or stop to break: ")

    if user_input.lower() == 'stop':
        break

    try:
        total_sum += float(user_input)
    except ValueError:
        print("Invalid input")

print(total_sum)

