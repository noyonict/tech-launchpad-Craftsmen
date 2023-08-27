def is_prime(num1,num2):
    list = []
    for number in range(num1,num2):
        if number >1:
            for i in range(2,number):
                if number % i == 0:
                    break
            else:
                list.append(number)
    return list

starting_number = int(input("Enter starting number: "))
ending_number = int(input("Enter ending number: "))
result = is_prime(starting_number, ending_number)
print(result)

