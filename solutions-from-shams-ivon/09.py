# 9. Loop & Condition Combined:

# Write a function called count_even_numbers that takes a list of numbers and 
# returns the count of even numbers in the list. 
# For example, for the list [1, 2, 3, 4, 5], the function should return 2.


def count_even_numbers(a_list_of_numbers):
    count_even = 0
    for number in a_list_of_numbers:
        if number % 2 == 0:
            count_even = count_even + 1

    return count_even


print(count_even_numbers([54, 67, 7, 34, 6]))
print(count_even_numbers([7, 8, 324, 9, 0, 5, -3, -78, -2]))

