prime_num = []
for i in range(2,50):
    for j in range(2, int((i/2)+1)):
        if i%j == 0 :
            break
    else:
        prime_num.append(i)

output = "Prime Numbers from 2 to 50 are: " + ", ".join(f"{item}" for item in prime_num)

print(output)

