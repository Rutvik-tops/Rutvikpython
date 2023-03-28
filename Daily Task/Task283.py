
"""

task : 1 : take input from user in terms of days and convert them into no. of years and months 

"""



# Take input
days = int(input(" Task 1 Enter no. of days: "))

years = days // 365
months = (days / 365) // 30


print("No. of years:", years)
print("No. of months:", months)




"""
Task : 2 : take input from user in terms of year and find that teh given year is leap year or not ?	
"""

year = int(input("Task 2 Please Enter year: "))

if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



"""
task : 3 : take input from user as a number and find that the given number is positive , negative or zero 
"""

# take input 
number = int(input(" Task 3 Enter a number: "))

# check if the number is positive, negative or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


"""
task : 4 : 
take input in terms of Fehrenhit from user and convert it into celccius

"""



fahrenheit = float(input(" Task 4 Enter temperature in Fahrenheit: "))

# calculate temperature in Celsius
#celsius = (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius : ", celsius)



"""
task : 5 : take 5 different subject input from user and find the percentage. Also identify the Grade of the student based on percentage 
"""


subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = float(total_marks / 500) * 100


print("Total marks:", total_marks)
print("Percentage:", percentage)


if percentage>=90:
    print("Grade : A+")
          
elif percentage>=80:
    print("Grade : A")
          
elif percentage>=70:
    print("Grade : B")

elif percentage>=60:
    print("Grade : C")
          
elif percentage>=50:
    print("Grade : D")

else:
   print("fail")
