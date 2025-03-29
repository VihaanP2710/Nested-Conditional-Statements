print("Select your ride: ")
print("1. Bike")
print("2. Car")

#take input of number 1 or 2
#select your ride
choice = int(input("Enter your selection: "))

#on choose option 1
if choice == 1:
    print("Type of Bike?")
    print("1. Scooty")
    print("2. Motorbike")

    #condition for selection
    choice2 = int(input("Enter your selection (again): "))
    if choice2 == 1:
        print("Congratulations! You have selected a Scooty")
    elif choice2 == 2:
        print("Congratulations! You have selected a Motorbike")
    else:
        print("No, select from options please")

#user option 2
elif choice == 2:
    print("Type of Car?")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("Enter your selection (again): "))

    if choice3 == 1:
        print("Congratulations! You have selected a Sedan")
    if choice3 == 2:
        print("Congratulations! You have selected an SUV")
    else:
        print("No, select from the options")
