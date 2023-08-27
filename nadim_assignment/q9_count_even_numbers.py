# Q9: Write a function called count_even_numbers that takes a list of numbers and returns the count of even numbers in the list. For example, for the list [1, 2, 3, 4, 5], the function should return 2.

def count_even_numbers(L):
    count = 0
    for i in L:
        if i%2 == 0:
            count+=1
        else:
            count = count
    return count


a = [1,2,3,4,5,8,9,19]    
print(count_even_numbers(a))

