"""
task : 5: take input from user as a word and find frequency of word in main string 


"""

# usinng input From user

Str1=input("Enter String:")

# using split parameter for string split

New_string=Str1.split(' ')

# Blank variable for count string

count=0


# using for loop

for i in New_string:

    # using if statement
    if  i == "Rutvik":
        count+=1
print("frequency of character 'Rutvik' is : ",count)
