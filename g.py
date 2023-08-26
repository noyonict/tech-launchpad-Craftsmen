
# While Loop & Condition:
# Implement a program where the user is repeatedly asked to enter numbers until they type 'stop'. Once they do, the program should display the sum of all the numbers entered.

def fun():
    sum=0
    while 1:
        num=input("Please enter a number : ").strip(' ')
        if(num=="stop"):
            break
        if num.isdigit():
            sum+=int(num)
        else:
            print("Please enter a number")
            

    print(sum)

fun()