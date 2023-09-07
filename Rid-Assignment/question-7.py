int_inputs = []

while True:
    try:
        int_input = input("Enter number or string: ")

        if int_input == 'stop':
            break
        else:
            int_inputs.append(int_input)

    except:
        print("Invalid Input")

sum = 0

for item in int_inputs:
    sum +=int(item)
print(sum)