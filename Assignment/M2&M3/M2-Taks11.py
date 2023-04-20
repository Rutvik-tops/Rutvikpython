#Taask:11:Write a Python program to unzip a list of tuples into individual lists


# Define a list of tuples
lst = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip the list of tuples into two separate lists
nums, letters = zip(*lst)

# Print the resulting lists
print(nums)    
print(letters) 
