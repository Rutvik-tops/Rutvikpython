#Task:8:Write a Python program to check whether a list contains a sublist.


list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4]

# loop through the list and check for a match
for i in range(len(list1)):
    if list1[i:i+len(list2)] == list2:
        print("List contains sublist")
        break
else:
    print("List does not contain sublist")
