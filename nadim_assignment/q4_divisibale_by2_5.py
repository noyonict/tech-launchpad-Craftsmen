# Q4: Expand the above program. If the number is divisible by both 2 and 5, print "This number is divisible by 2 and 5."

number = int(input("Input your number: ").strip())


if number%2 == 0 and number%5 == 0:
    print("This number is divisible by 2 and 5")
else:
    print("This number is NOT divisible by either 2 or 5 or both 2 and 5")