#take 5 friut input from user and print list in vertical line

fruit_list=[]

for i in range(1,6):
    fruit=input("Enter Fruit: ")

    fruit_list.append(fruit)

for i in fruit_list:
    print("Your Fruit:",i)
