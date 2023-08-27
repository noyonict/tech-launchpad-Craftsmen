# Introduction to Python:

## Questions:

1. Write a simple Python program that prints "Hello, World!" to the console?

   ```py
   print("Hello World!")
   ```

2. Python Basics – Variables:
   Create a program that prompts the user for their name and age, then stores these in variables and prints a message saying, "Hello, [name]! You are [age] years old."

   ```py
   name = input("Please enter your name: ")
   age = input("Please enter your age: ")
   print(f"Hello, {name}! You are {age} years old.")
   ```

3. Conditions – If, Else, Elif:
   Write a program that asks the user for a number and prints whether the number is even or odd.

   ```py
   number = int(input("Please enter your number: "))
   if number % 2 == 0:
      print(f"The number you have entered is even.")
   else:
      print(f"The number you have entered is odd.")
   ```

4. Conditions – Example:
   Expand the above program. If the number is divisible by both 2 and 5, print "This number is divisible by 2 and 5."

   ```py
   number = int(input("Enter a number: "))

   if number % 2 == 0 and number % 5 == 0:
       print("This number is divisible by 2 and 5.")
   elif number % 2 == 0:
       print("This number is only divisible by 2.")
   elif number % 5 == 0:
       print("This number is only divisible by 5.")
   else:
       print("This number is not divisible by 2 or 5.")
   ```

5. Condition & Loop – Basics:
   Create a program that uses a loop to print numbers from 1 to 10. For each number, if it's even, print "[number] is even". If it's odd, print "[number] is odd".

   ```py
   for i in range(1, 11):
      if i % 2 == 0:
         print(f"{i} is even.")
      else:
         print(f"{i} is odd.")
   ```

6. For Loop and Condition:
   Write a program that uses a for loop to print all the prime numbers between 2 and 50.

   ```py
   def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

   for i in range(2, 51):
      if is_prime(i):
         print(i)
   ```

7. While Loop & Condition:
   Implement a program where the user is repeatedly asked to enter numbers until they type 'stop'. Once they do, the program should display the sum of all the numbers entered.

   ```py
   sum = 0
   while True:
      user_input = input("Please enter your number. If you want to exit, type 'stop': ")

      if user_input == "stop":
         print(f"The sum of all the numbers you've entered so far is {sum}")
         break
      else:
         sum += int(user_input)
   ```

8. Functions:
   Define a function called multiply. This function should take two parameters and return their product. Test your function with several pairs of numbers to ensure it works correctly.

   ```py
   def multiplier(a, b):
      return a * b

   # Test the function with different pairs of numbers
   print(multiply(2, 3))   # Output: 6
   print(multiply(5, -4))  # Output: -20
   print(multiply(0, 7))   # Output: 0
   print(multiply(-2, -2)) # Output: 4

   ```

9. Loop & Condition Combined:
   Write a function called count_even_numbers that takes a list of numbers and returns the count of even numbers in the list. For example, for the list [1, 2, 3, 4, 5], the function should return 2.

   ```py
   def count_even_numbers(number_list):
      count = 0
      for number in number_list:
         if number % 2 == 0:
            count += 1
   return count

   tester_list = [1, 2, 3, 4, 5]
   even_count = count_even_numbers(tester_list)
   print(f"The number of even numbers in this list is {even_count}")
   ```

10. Final Challenge – Comprehensive:
    Create a program that does the following:
    Defines a function is_prime which checks if a number is prime.
    Prompts the user to enter a range (two numbers).
    Uses a loop to go through the numbers in the given range.
    Prints out all prime numbers in that range.

    ```py
    def is_prime(n):
      if n <= 1:
         return False
      if n <= 3:
          return True
      if n % 2 == 0 or n % 3 == 0:
          return False
      i = 5
      while i * i <= n:
          if n % i == 0 or n % (i + 2) == 0:
              return False
          i += 6
      return True

      a = int(input("Print the first number of your deisred range: "))
      b = int(input("Print the last number of your deisred range: "))

      for i in range(a, b + 1):
         if is_prime(i):
            print(i)
    ```
