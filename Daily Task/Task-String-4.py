"""
task : 4: take input from user in terms of character and find frequency of that6 character in string 

	eg: Enter string : Good Morning 
	    Enter character : o

		frequency of character 'o' is : 3

"""
Str1=input("Enter String:")

count=0

for i in Str1:
    if  i == "A":
        count+=1
print("frequency of character 'A' is : ",count)
