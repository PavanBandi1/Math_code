# Simple math Ca1lculations

while True:
    try:
        start = input("Do you want to start the math operations:")
        if(start == "yes"):
            Number = int(input("Enter frst number:"))
            Number1 = int(input("Enter second number:"))
            option = input("Enter which operation you want:")
            if(option == "Addition"):
                addition = Number+Number1
                print(f"Addition of two numbers is:{addition}")
            elif(option == "Subraction"):
                Subraction = Number-Number1
                print(f"Subraction of two numbers is:{Subraction}")
            elif(option == "Multiplication"):
                Multiplication = Number*Number1
                print(f"Multiplication of two numbers is:{Multiplication}")
            elif(option == "Division"):
                Division = Number/Number1
                print(f"Division of two numbers is:{Division}")
            continue
        elif(start == "no"):
                print("Thank you......")
                break
    except ValueError as err:
        print(f"please enter a number:{err}")
        
    else:
        break
     
