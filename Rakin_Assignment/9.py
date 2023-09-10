def count_even_numbers(numbers_list):
    count = 0
    for num in numbers_list:
        if num % 2 == 0:
            count += 1
    return count

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = count_even_numbers(input_list)
print("Even numbers in the list:", even_count)
