

num_list = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)

user_guess = num_list[:5]
print(user_guess)
c_guess = num_list[5:]
print(c_guess)

import random

for i in range(5):  # repeat the process 5 times
    print("Round", i+1)
    for j in range(1):  # generate 5 random numbers in each round
        num1 = random.randint(1, 100)  # generate a random number between 1 and 100
        print("Lucky Number : ",num1)
        if num1 in user_guess:

            user_guess.remove(num1)
            print(user_guess)
        
        elif num1 in c_guess:
            c_guess.remove(num1)
            print(c_guess)
        
    print()  #Blank print
if user_guess==0:
    print("Winner User Guess")
elif c_guess==0:
    print("Winner c Guess")
else:
    print("Gaame Over") 

    
