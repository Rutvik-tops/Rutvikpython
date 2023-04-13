"""
task : 3: Count How many digits are there in a string 

	eg: Hello I'm 5 yrs old and I have 10 Chocolates
	digit_count=3
"""
# take inout from user 
Str1=input("Enter String :")

# Take blank variable 
count=0

# using for loop

for i in Str1:

    # using if statement
    
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        count+=1

print(" Digit in String : ",count)
