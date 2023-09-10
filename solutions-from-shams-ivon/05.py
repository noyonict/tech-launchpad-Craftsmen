# 5. Condition & Loop – Basics:

# Create a program that uses a loop to print numbers from 1 to 10. 
# For each number, if it's even, print "[number] is even". 
# If it's odd, print "[number] is odd".


for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

