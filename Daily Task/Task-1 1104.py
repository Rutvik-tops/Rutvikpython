
#task: 1 
# create an empty list to store the user input
user_input = []

# take 10 elements from the user and append to the user_input list
for i in range(10):
    element = int(input("Enter element: "))
    user_input.append(element)

# create empty lists 
even_list = []
odd_list = []


for num in user_input:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Even numbers list:", even_list)
print("Odd numbers list:", odd_list)
