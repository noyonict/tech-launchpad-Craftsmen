# For Loop and Condition:
# Write a program that uses a for loop to print all the prime numbers between 2 and 50.

def fun():
    for i in range(2,50):
        ok=0
        for j in range(2,i):
            if i%j==0 :
                ok=1

        if ok==0 :
            print(i)

fun()