
# Take Input From User

M1=int(input("Enter First Exam Mark  :"))
#Nested If Condition
if M1>=60:
    print("You Have Clear First Exam ")

    M2=int(input("Enter Second Exam Mark  :"))    
    if M2>=70:
        print("You Have Clear Second Exam ")
        M3=int(input("Enter Third Exam Mark  :"))
        if M3>=80:
              print("You have clear Third Exam ")
        else:
              print("Fail in Third Exam !!! ")
    else:
         print("Fail in Second Exam !!! ")
else:
    print("Fail in First Exam !!! ")
        
