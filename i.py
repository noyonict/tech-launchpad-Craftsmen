# Loop & Condition Combined:
# Write a function called count_even_numbers that takes a list of numbers and returns the count of even numbers in the list. For example, for the list [1, 2, 3, 4, 5], the function should return 2.

def count_even_numbers(nummbers):
    count=0
    for number in (nummbers):
        if number%2==0: 
            count+=1
    return count

numbers=[1,2,3,4,5]
print(count_even_numbers(numbers))
