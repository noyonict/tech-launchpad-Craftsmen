def count_even_numbers(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    return even_count
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_even_numbers(numbers)
print("Number of EVEN numbers: ", result)
