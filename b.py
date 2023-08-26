# Python Basics – Variables:
# Create a program that prompts the user for their name and age, then stores these in variables and prints a message saying, "Hello, [name]! You are [age] years old."
def fun(name, age):
    out=f"Hello, {name}! You are {age} years old."
    print(out)

name=input("Enter your name : ").strip(' ')
age=input("Enter your age : ").strip(' ')

fun(name, age)