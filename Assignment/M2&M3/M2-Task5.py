"""
Task : 5 :Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
string is less than 3, leave it unchanged

"""
# Take String input from user 
s = input("Enter a string: ")

# using ladder if

if len(s) < 3:
    print(s)
elif len(s)>3:
    print(s)
    s.endswith('ing')
    print(s + 'ly')     

else:
    print("Your lenght is lesser then 3")

