# Final Challenge – Comprehensive:
# Create a program that does the following:
# Defines a function is_prime which checks if a number is prime.
import math

def prime_check(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
        
    return True

# Prompts the user to enter a range (two numbers).

lower_range =int(input("Enter lower range : "))
upper_range =int(input("Enter upper range : "))

if lower_range>upper_range:
    tmp=lower_range
    lower_range=upper_range
    upper_range=tmp

# Uses a loop to go through the numbers in the given range.

prime_numbers=0
for current in range(lower_range,upper_range+1): 
    if current==1 :
        continue

    is_prime =prime_check(current)
    if is_prime==True:
        prime_numbers+=1

# # Prints out all prime numbers in that range.

print(prime_numbers)