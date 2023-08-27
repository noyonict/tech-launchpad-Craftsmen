# Condition & Loop – Basics:
# Create a program that uses a loop to print numbers from 1 to 10. For each number, if it's even, print "[number] is even". If it's odd, print "[number] is odd".

def fun():
    for i in range(1,11):
        if i%2==0 :
            print(i, "is even")
        else :
            print(i, "is odd")

fun()