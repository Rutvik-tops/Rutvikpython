def areafinder(length, width):
    
    return length * width


print("=============Area Finder=============")
print("1. Circle")
print("2. Triangle")
print("3. Rectangle\n")

choice = int(input("Enter Choice : "))

if choice == 3:
    length = float(input("Enter Length : "))
    width = float(input("Enter Width : "))

    area = areafinder(length, width)
    print("Area of Rectangle : ", area)
elif choice == 2:
    length = float(input("Enter Length : "))
    width = float(input("Enter Number : "))

    area = areafinder(length,width)
    print("Area of Triangle",area)

elif choice == 1:
    length = float(input("Enter Length : "))
    width = float(input("Enter Number : "))

    area = areafinder(length,width)
    print("Area of Circle",area)

    
else:
    print("Invalid Choice")

print("\n>>>>>>>>>>>>>Thank You ")
