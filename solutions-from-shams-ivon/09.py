def count_even_numbers(a_list_of_numbers):
    count_even = 0
    for number in a_list_of_numbers:
        if number % 2 == 0:
            count_even = count_even + 1

    return count_even


print(count_even_numbers([54, 67, 7, 34, 6]))
print(count_even_numbers([7, 8, 324, 9, 0, 5, -3, -78, -2]))

