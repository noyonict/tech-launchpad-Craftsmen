count_even_numbers = lambda x: x % 2 == 0
input_list = list(map(int, input().split()))
print(len(list(filter(count_even_numbers, input_list))))
