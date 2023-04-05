
#Task-4

#Nested for loop

#outer for loop

for i in range(5,0,-1):

    # inner for loop 
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")

    print()
