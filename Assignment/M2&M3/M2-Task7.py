#Task : 7 : Program to find Greatest Common Divisor of two numbers.
#For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.



# take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a<b :
    smallernum= a
else:
    smallernum = b
# using for loop 
for i  in (1,smallernum+ 1):
    if a%i==0 and b%i==0:
        GCD=i

# Print the GCD
print("The GCD of", a, "and", b, "is", a)
