def count_even_numbers(numbers):
    count = 0
    for item in numbers:
        if item % 2 ==0:
            count += 1
    return count

result = count_even_numbers([1,2,3,4,5,6])
print(result)


