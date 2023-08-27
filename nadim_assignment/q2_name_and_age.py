# Q2: Create a program that prompts the user for their name and age, then stores these in variables and prints a message saying, "Hello, [name]! You are [age] years old."

name = input("Enter your name: ")
age = input("Enter your age: ")


name = name.strip().title()
age = age.strip()


print(f"Hello, {name}! You are {age} years old.")