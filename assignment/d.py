# Conditions – Example:
# Expand the above program. If the number is divisible by both 2 and 5, print "This number is divisible by 2 and 5."

def check(num):
    if num%2==0 & num%5==0:
        print("This number is divisible by 2 and 5.")
    else : 
        print("This number is not divisible by 2 and 5.")

num=int(input("Enter a number : "))

check(num)