# Q7: Implement a program where the user is repeatedly asked to enter numbers until they type 'stop'. Once they do, the program should display the sum of all the numbers entered.

total = 0
while True:
    number = input("Enter a number: ")
    if number == 'stop':
        break
    try :
        num = int(number)
    except:
        print('Invalid Input')
        continue  
    total = total + num
print (total)
