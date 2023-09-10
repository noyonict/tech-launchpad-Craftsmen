# 6. For Loop and Condition:

# Write a program that uses a for loop to print 
# all the prime numbers between 2 and 50.


for number in range(2, 51):
    is_prime = True
    for checker_number in range(2, number):
        if checker_number * checker_number > number:
            break
        
        if number % checker_number == 0:
            is_prime = False
            break

    if is_prime:
        print(number)

