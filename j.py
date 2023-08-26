# Final Challenge – Comprehensive:
# Create a program that does the following:
# Defines a function is_prime which checks if a number is prime.
import math

def prime_check(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
        
    return True
