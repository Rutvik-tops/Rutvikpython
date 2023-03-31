
#Take input From User

N1=int(input("Enter Number 1 :"))
N2=int(input("Enter Number 2 :"))
N3=int(input("Enter Number 3 :"))

#using Nested Method

if N1>N2:
    if N1>N3:
        print("Largest Number Is N1",N1)
    else:
        print("Largest Number Is N3",N3)
else:
    if N2>N3:
         print("Largest Number Is N2",N2)
    else:
         print("Largest Number Is N3",N3)
        
        
        
