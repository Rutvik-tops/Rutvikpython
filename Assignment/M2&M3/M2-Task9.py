
#Task:9:Write a Python program to find the second smallest number in a list. 

numbers = [2, 5, 7, 3, 9, 4]

if len(numbers) < 2:
    print("No second smallest number")
else:
    smallest = second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
            
    print("Second smallest number in the list is:", second_smallest)
