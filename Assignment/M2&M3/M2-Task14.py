

#Task:14:Write a Python program to find the highest 3 values in a dictionary
my_dict = {'a': 300, 'b': 200, 'c': 500, 'd': 100, 'e': 400}

# Using the sorted() function to sort the values in descending order
sorted_values = sorted(my_dict.values(), reverse=True)

# Slicing the first three elements of the sorted list to get the highest 3 values
highest_values = sorted_values[:3]

print("The highest 3 values in the dictionary are:", highest_values)
