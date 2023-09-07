def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


first_number = int(input("Print the first number of your deisred range: "))
last_number = int(input("Print the last number of your deisred range: "))

for i in range(first_number, last_number + 1):
    if is_prime(i):
        print(i)
