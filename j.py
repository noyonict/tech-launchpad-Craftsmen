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