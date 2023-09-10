sum = 0

while('stop'):
    number = input("enter number: ")
    if number.isnumeric():
        sum += int(number)
    else:
        break
    continue
print(sum)


