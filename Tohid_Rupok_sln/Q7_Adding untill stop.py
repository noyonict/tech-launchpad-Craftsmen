num = input("Enter a number: ")

all_num = []
sum = 0
while num != "stop":
    try:
        sum = sum + float(num)
        all_num.append(num)
        num = input("Great! Enter a number again: ")
    except:
        num = input(f"'{num}' is not a number. Please, Enter a number or type 'stop' to finish the programme: ")
        
total_num = len(all_num)

if total_num == 1:
    print(f"You have only entered {total_num} number: {all_num}")
elif total_num == 0:
    print("You didn't enter any number")
else:
    print(f"Congratulations! You have Successfully entered {total_num} numbers")
    print(f"You have entered: {all_num}")
    print(f"The sum of all number you have entered is {sum}")

