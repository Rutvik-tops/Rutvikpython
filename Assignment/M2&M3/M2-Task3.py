#Task: 3 : Write a Python program to count the occurrences of each word in a given sentence.

Str1=input("Enter string")


Str1=Str1.split(" ")

i = 0
while i <len(Str1):

    count=0

    for j in Str1:
            if Str1[i] == j:
                count+=1

    print(Str1[i],"Present",count,"Time")
    i=i+1
