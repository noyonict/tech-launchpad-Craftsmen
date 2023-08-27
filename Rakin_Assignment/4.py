user_number = int(input("Give a number "))

if(user_number % 2 == 0 and user_number%5 == 0):
    print(f"{user_number} the number can de divided by both 2 and 5")
elif(user_number%2 !=0):
    print(f"{user_number} is odd")
else:
    print(f"{user_number} no operations can be performed")