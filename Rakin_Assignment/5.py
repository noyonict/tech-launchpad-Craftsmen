user_input = int(input("Enter the range : "))

for i in range(1,user_input+1):
       if(i % 2 == 0):
         print(f"{i} is even")
       else:
        print(f"{i} is odd")