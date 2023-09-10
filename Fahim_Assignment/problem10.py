#10. Final Challenge – Comprehensive:
# Create a program that does the following:
# Defines a function is_prime which checks if a number is prime.
# Prompts the user to enter a range (two numbers).
# Uses a loop to go through the numbers in the given range.
# Prints out all prime numbers in that range.

a=int(input("Enter a value: "))
b=int(input("Enter a value: "))

def is_prime(a,b):
    list = []
    for number in range (a, b):    
        for i in range (2, number):  
            if number % i == 0:  
                break  
        else:  
             list.append(number) 
    return list

result = is_prime(a,b)

print(result)
    



