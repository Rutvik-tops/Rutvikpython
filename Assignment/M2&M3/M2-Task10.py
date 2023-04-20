"""
#Task:10:Write a Python program to get unique values from a list

"""
l1 = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]

#Take blank variable

unique_l1 = []


# using for loop

for element in l1:
    if element not in unique_l1:
        #using append method
        unique_l1.append(element)

print(unique_l1)
