#9. Loop & Condition Combined:
# Write a function called count_even_numbers that takes a list of numbers and 
# returns the count of even numbers in the list. For example, for the list [1, 2, 3, 4, 5], the function should return 2

list = []
user_input = input("Enter a number: ")
list = user_input.split(',')
list=[int(item) for item in list]

def count_even_numbers(list):
    count = 0
    for i in list:
        if i % 2 == 0:
          count += 1
    return count

result = count_even_numbers(list)

print(result)
    





