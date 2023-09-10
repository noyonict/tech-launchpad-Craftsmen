# 7. While Loop & Condition:
# Implement a program where the user is 
# repeatedly asked to enter numbers until they type 'stop'. Once they do, the program should display the sum of all the numbers entered.
list = []
while True:
    user_input = input("Enter a number: ")
    if user_input == 'stop':
        break
    list.append(user_input)
    convert_to_integer=[int(item) for item in list]  
total_sum = sum(convert_to_integer)

print(total_sum)

    
