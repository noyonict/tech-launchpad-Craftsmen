user_input = input("Enter a Number: ")

while True:
    try:
        number = int(user_input)
        break
    except: 
        try:
            number = float(user_input)
            user_input = input(f"'{user_input}' is a float number. Please, Enter an integer number: ")
        except:
            user_input = input(f"'{user_input}' is a string. Please, Enter an integer Number: ")
if number % 2 == 0:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")

if number % 2 == 0 and number % 5 == 0:
    print(f"{number} is divisible by 2 and 5.")
elif number % 2 == 0:
    print(f"{number} is only divisible by 2 not 5.")
elif number % 5 == 0:
    print(f"{number} is only divisible by 5 not 2.")
else:
    print(f"{number} is not divisible by 2 or 5.")
