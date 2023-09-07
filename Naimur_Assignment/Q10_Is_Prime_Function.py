def is_prime(numbers):
  if numbers <= 1:
    return False
  if numbers == 2:
    return True
  if numbers % 2 == 0:
    return False
  for i in range(2, int(numbers**0.5) + 1):
    if numbers % i == 0:
      return False
  return True

while True:
  try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    if start <= 2:
      print(f"Prime numbers in the range {start} to {end}: ")
    for num in range(start, end + 1):
      if is_prime(num):
        print(num)
    break

  except ValueError:
    print("Invalid input. Please enter valid integers for the range.")
        