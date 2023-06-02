user='''
    1) Manager
    2) Customer        
'''

manager_option='''
        1) Add Fruit
        2) View Fruit
        3) Update Fruit
'''



name=None
price=None
qty=None
Fruit={}
add={}
def add_fruit():
    add[name]={'price':price,'qty':qty}
    Fruit.update(add)
def view_fruit():
    add[name]={'price':price,'qty':qty}
    Fruit.update(add)
    print(Fruit)

def update_fruit():
    pass

status=True

print(user)
choice= int(input("Select Your roll  : "))
while status:


    if choice==1:
        
            print(manager_option)
            manager_choice=int(input("Enter choice : "))
            if manager_choice==1:
                name=input("Enter Name of fruit : ")
                price=int(input("Enter Price : "))
                qty=int(input("Enter Quantity : "))
                add_fruit()
                
            elif manager_choice==2:
                print(" View Fruit Stock ")

                Fruit[name]={"KG":qty,"Price":price}
                print(" View Your Fruit Stock ",Fruit)

            elif manager_choice==3:
                print("Update Fruit")
                name=input("Enter Name of fruit : ")
                price=int(input("Enter Price : "))
                qty=int(input("Enter Quantity : "))
                add_fruit()
            else:
                print("Invalid choice")
                print("Try Again")
            method_option=input("Do You want to Continue : ['y/n'] : ")
            if method_option=='y' or method_option=='yes':
                status=True
            else:
                status=False
                break      
    else:
        pass
       

else:
     pass
        
        