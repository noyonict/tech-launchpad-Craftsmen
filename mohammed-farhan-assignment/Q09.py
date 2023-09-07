def count_even_numbers(number_list):
    count = 0
    for number in number_list:
        if number % 2 == 0:
            count += 1
    return count


tester_list = [1, 2, 3, 4, 5]
even_count = count_even_numbers(tester_list)
print(f"The number of even numbers in this list is {even_count}")
