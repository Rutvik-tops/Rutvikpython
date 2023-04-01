#WAP to take 10 Number of input from user and check  the number is even or odd Then after give sum of Even num and odd number 


even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0


#use For loop

for i in range(0,10):
    num = int(input("Enter a number: "))
    
    #Using conditional statement for check condition
    
    if num % 2 == 0:
         even_count += i #You can write: even_count = even_count + i 
         even_sum += num
     
    else:
        odd_count += i
        odd_sum += num
        
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)
print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)


    
