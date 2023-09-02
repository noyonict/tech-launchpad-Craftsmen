total = 0
while True:
    user_input = input("Enter a number or type 'stop' to exit: ")
    if user_input.lower() == 'stop':
        break
    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'stop'.")
print("Sum of all numbers entered: ", total)
