"""
Task: 4 :Write a Python program to get a single string from two given strings, separated by a space and swap the first
two characters of each string.

"""

# take input from user

str1=input("Enter String :")

print("Original string : ",str1)


#String Slicing
#index
print("Updated String : ",str1[-1:]+str1[1:-1]+str1[0:1])

