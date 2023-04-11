import random

# computer's guess
computer_guess = random.randint(1, 100)

# chances
num_chances = 5

print(" guess  number Game" )

# using  For loop
for i in range(5):
    # Get the user's guess
    user_guess = int(input("Enter a number between 1 and 100: "))
    
    # Check condition 
    if user_guess == computer_guess:
        print("Congratulations! You guessed the number!")
        break
    
    elif user_guess < computer_guess:
        print("Hint: Think of a higher number.")
    else:
        print("Hint: Think of a lower number.")
    
    # Chances
    num_chances -= 1
    print(f"Chances left: {num_chances}")
    
    
    if num_chances == 0:
        print("GAME OVER")
