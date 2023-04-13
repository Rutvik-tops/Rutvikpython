"""
task : 2: Identify no. of vowels and consonants from the string 
	eg: Good Morning 
	voewl_count=4
	consonant_count=7
	white_space=1
"""

# Take input from user

Str1=input("Enter input : ")

# take blank variable

vowel_count=0
consonant_count=0
White_Space=0



# using for loop

for i in Str1:

# using ladder if statement

    if i in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    
    elif i.isalpha():
        consonant_count += 1

    elif i.isspace():
        whitespace_count += 1

print("vowel_count =", vowel_count)
print("consonant_count =", consonant_count)
print("whitespace_count =", White_Space)
