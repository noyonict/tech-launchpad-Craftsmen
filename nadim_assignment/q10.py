# Q10: Create a program that does the following: 
# Defines a function is_prime which checks if a number is prime. 
# Prompts the user to enter a range (two numbers). 
# Uses a loop to go through the numbers in the given range. 
# Prints out all prime numbers in that range.

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


start = int(input("starting value: "))
end = int(input("ending value: "))


for i in range(start, end+1):
    if is_prime(i) == True:
        print(i)

