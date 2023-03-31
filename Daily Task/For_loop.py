#WAP to using For loop and print 10 time Hello Print

for i in range(0,10):
    print("Hello")

#WAP to using For loop and print 6 time Hello Print With Numbers


for i in range(0,6):
    print(i+1,")Hello")


#WAP to take input from user 5 time using the for loop

for i in range(1,6):
    a=input("Enter Name : ")

#WAP to print reverse range using for loop

#Step has given as -1

for i in range(10,0,-1):
    print(i)

#WAP to print even and odd numbers from thr given range

for i in range(1,11):
    print(i,end=" ")
    if i%2 == 0:
        print("-Even")
    else:
        print("-Odd")
