# task :1 : Identidy the white spaces in a string


str1=input("Enter string:")

count=0

for i in str1:
    if i==" ":
        count+=1

    
print("White space in string is : ",count) 
