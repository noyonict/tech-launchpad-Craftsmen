# Take input from uers
input_range = input("Enter the range of number from which you want to find out the prime numbers (use '-' as a separator of range): ")

# Separate two number\
while True:
    two_num = list(input_range.split("-"))
    try:
        first_num = int(two_num[0])
        last_num = int(two_num[1])
        break
    except:
        input_range = input("Invalid input. Please enter a range of number using dash(-) as a separator: ")

# create function to test a num is prime or not
def is_prime (num):
	for i in range(2,int((num/2)+1)):
		if num%i == 0:
			break
	else:
			num = "prime"
			return (num)

# loop through the all numbers in the range and check which are prime using is_prime function and keep those prime num in a list called prime_num
prime_num = []
for x in range(first_num, last_num):
    if is_prime(x) == "prime":
        prime_num.append(x)

# print all the prime num in the list without the third bracket
ipn = ','.join(map(str,prime_num))
if len(prime_num)<1:
    print(f"There is no prime number between {first_num} and {last_num}.")
elif len(prime_num) == 1:
    print(f"There is only one prime number between {first_num} & {last_num} which is {ipn}")
else:
    print(f"There are {len(prime_num)} prime numbers between {first_num} & {last_num}: {ipn}.")
