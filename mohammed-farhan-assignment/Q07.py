sum = 0
while True:
    user_input = input(
        "Please enter your number. If you want to exit, type 'stop': ")
    if user_input == "stop":
        print(f"The sum of all the numbers you've entered so far is {sum}")
        break
    else:
        sum += int(user_input)
