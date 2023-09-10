#4. Conditions – Example:
# Expand the above program. If the number is divisible by both 2 and 5, print "This number is divisible by 2 and 5."

number= int(input("Enter a number: "))
if number % 2== 0 and number % 5 ==0:
        print(f"This {number} is divisible by 2 and 5.")
# else:
#         print(f"{number} is odd.")
        
elif number % 2 == 0:
    print(f"{number} is even.")

elif not number % 2 == 0:
    print(f"{number} is odd.")