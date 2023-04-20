

#Taask:13:Write a Python program to sort a dictionary (ascending /descending) by value.

# Sample dictionary
d = {'apple': 5, 'banana': 3, 'orange': 7, 'kiwi': 2}

# Sorting the dictionary in ascending order by value
asc_dict = dict(sorted(d.items(), key=lambda x: x[1]))

# Sorting the dictionary in descending order by value
desc_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

# Printing the sorted dictionaries
print("Ascending Order:", asc_dict)
print("Descending Order:", desc_dict)
