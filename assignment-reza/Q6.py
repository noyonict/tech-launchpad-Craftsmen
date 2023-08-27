for prime_num in range(2,51):
    is_prime = True
    for i in range(2,prime_num):
        if prime_num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(prime_num)