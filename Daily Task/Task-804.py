#enter input from user and check eligibility for discountand after give discount customer

discount_Amount=0
Total_payment_amount=0

#using input method

Name=input("Enter Your Name: ")
age=int(input("Enter your Age:"))
total_amount=int(input("Enter your total amount:"))

#ladder condition Statement

if age >= 18 and age <= 30 and total_amount >= 5000:
    discount =20
elif age > 30 and age <= 50 and total_amount >= 5000:
    discount = 30
elif age > 50 and total_amount >= 5000:
    discount = 50
else:
    discount = 0

#sum for  discount
    
discount_Amount = total_amount * discount/100
   
Total_payment_amount=total_amount-discount_Amount

print("===========INVOICE===========")

print("Name : ",Name)
print("age : ",age)
print("total_amount : ",total_amount)
print("Discount amount : ",discount_Amount)
print("Total amount : ",Total_payment_amount)


