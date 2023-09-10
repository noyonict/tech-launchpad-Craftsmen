# 3. Conditions – Example:

# Expand the above program. If the number is divisible by both 2 and 5, 
# print "This number is divisible by 2 and 5."


number = int(input("Enter a number: "))
remainder_2 = number % 2
remainder_5 = number % 5

if remainder_2 == 0 and remainder_5 == 0:
    print(f"{number} is divisible by both 2 and 5")
else:
    print(f"{number} is not divisible by both 2 and 5")

