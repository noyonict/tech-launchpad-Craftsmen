def multiply(x,y):
    result = x*y
    return result

while True:
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = multiply(num1, num2)
        print(f"The multiplication of {num1}, {num2}: {result}")
        break

    except:
        print("Invalid input. Please enter valid numbers.")
              
