# Task-2

# Nested for loop
 #outer for loop 
for i in range(1,6):

    #inner for loop
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
