n = 50
flag_prime_or_not = [True]*(n+1)
flag_prime_or_not[0]=flag_prime_or_not[1]=False


n_root = int(n**0.5)+1

for num in range(2,n_root):
    if flag_prime_or_not[num]:
    	for i in range(num*num,n+1,num):
        	    flag_prime_or_not[i] = False
       	 
 
prime_numbers = [prime for prime, flag in enumerate(flag_prime_or_not) if flag]	 

print(prime_numbers)
