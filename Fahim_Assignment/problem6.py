#6. For Loop and Condition:
# Write a program that uses a for loop to print all the prime numbers between 2 and 50.

for number in range (2, 51):    
        for i in range (2, number):  
            if number % i == 0:  
                break  
        else:  
            print (f"{number}", end=" ")  