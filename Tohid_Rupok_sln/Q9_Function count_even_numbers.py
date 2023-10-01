list = [23,56,7,8,9,43,55,66,68]
def count_even_numbers(list):
    even_num = []
    for num in list:
        if num % 2 == 0:
            even_num.append(num)
    count = len(even_num)
    return count

total_even_num = count_even_numbers(list)
print(f"Total Even Number: {total_even_num}")
