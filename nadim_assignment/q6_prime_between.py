# Q6: Write a program that uses a for loop to print all the prime numbers between 2 and 50.

for n in range(2, 51):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n, end=", ")
