def is_prime(lower_range,upper_range):
         for number in range(lower_range,upper_range+1):
           if number>1:
             for i in range(2,number):
                  if (number % i) == 0:
                   break
             else:
              print(number)

lower_range = int(input("Please enter a starting range : "))
upper_range = int(input("Please enter a starting range : "))
is_prime(lower_range,upper_range)