print("~~~Welcome to Shakes & Fries~~~")
print("We'd love to take your order\n\n")

shake_yes_no = input("Would you like a shake? Y/N\n")

if shake_yes_no == "y" or shake_yes_no == "Y":
    print("~~ Shake Menu ~~~")
    print("\tV : Vanilla    ($3)")
    print("\tC : Chocolate  ($3)")
    print("\tS : Strawberry ($3)")
    print("\tN : Neapolitan ($5)")
    shake_choice = input("Please make a selection from the above:\n")
    if shake_choice != "V" and shake_choice != "C" and shake_choice != "S" and shake_choice != "N":
        print(f"{shake_choice}: Invalid selection")
        fries_yes_no = input("Would you like fries? Y/N\n")
        if fries_yes_no == "n" or fries_yes_no == "N":
            print("\n~~~Order Summary~~~")
            print("Not Hungry? That's OK... Have a nice day!")
        else:
            print("~~ Fries Menu ~~~")
            print("\tA : Animal Fries ($4)")
            print("\tC : Cheese Fries ($3)")
            print("\tF : French Fries ($2)")
            fries_choice = input("Please make a selection from the above:\n")
            if fries_choice != "A" and fries_choice != "C" and fries_choice != "F":
                print(f"{fries_choice}: Invalid selection")
                if (shake_choice != "V" and shake_choice != "C" and shake_choice != "S" and shake_choice != "N") and (fries_choice != "A" and fries_choice != "C" and fries_choice != "F"):
                    print("\n~~~Order Summary~~~")
                    print("Not Hungry? That's OK... Have a nice day!")
            else:
                if fries_choice == "A":
                    print("\n~~~Order Summary~~~")
                    print("Animal Fries")
                    print("Your total is: $4")
                elif fries_choice == "C":
                    print("\n~~~Order Summary~~~")
                    print("Cheese Fries")
                    print("Your total is: $3")
                elif fries_choice == "F":
                    print("\n~~~Order Summary~~~")
                    print("French Fries")
                    print("Your total is: $2")
    else:
        fries_yes_no = input("Would you like fries? Y/N\n")
        if fries_yes_no == "y" or fries_yes_no == "Y":
            print("~~ Fries Menu ~~~")
            print("\tA : Animal Fries ($4)")
            print("\tC : Cheese Fries ($3)")
            print("\tF : French Fries ($2)")
            fries_choice = input("Please make a selection from the above:\n")
            if fries_choice != "A" and fries_choice != "C" and fries_choice != "F":
                print(f"{fries_choice}: Invalid selection")
                if shake_choice == "V":
                    print("\n~~~Order Summary~~~")  # menu for shake only
                    print("Vanilla Shake")
                    print("Your total is: $3")
                elif shake_choice == "C":
                    print("\n~~~Order Summary~~~")
                    print("Chocolate Shake")
                    print("Your total is: $3")
                elif shake_choice == "S":
                    print("\n~~~Order Summary~~~")
                    print("Strawberry Shake")
                    print("Your total is: $3")
                elif shake_choice == "N":
                    print("\n~~~Order Summary~~~")
                    print("Neapolitan Shake")
                    print("Your total is: $5")
            else:  # fries and shake
                if shake_choice == "V":
                    if fries_choice == "A":
                        print("\n~~~Order Summary~~~")
                        print("Vanilla Shake, and Animal Fries")
                        print("Your total is: $7")
                    elif fries_choice == "C":
                        print("\n~~~Order Summary~~~")
                        print("Vanilla Shake, and Cheese Fries")
                        print("Your total is: $6")
                    elif fries_choice == "F":
                        print("\n~~~Order Summary~~~")
                        print("Vanilla Shake, and French Fries")
                        print("Your total is: $5")
                elif shake_choice == "C":
                    if fries_choice == "A":
                        print("\n~~~Order Summary~~~")
                        print("Chocolate Shake, and Animal Fries")
                        print("Your total is: $7")
                    elif fries_choice == "C":
                        print("\n~~~Order Summary~~~")
                        print("Chocolate Shake, and Cheese Fries")
                        print("Your total is: $6")
                    elif fries_choice == "F":
                        print("\n~~~Order Summary~~~")
                        print("Chocolate Shake, and French Fries")
                        print("Your total is: $5")
                elif shake_choice == "S":
                    if fries_choice == "A":
                        print("\n~~~Order Summary~~~")
                        print("Strawberry Shake, and Animal Fries")
                        print("Your total is: $7")
                    elif fries_choice == "C":
                        print("\n~~~Order Summary~~~")
                        print("Strawberry Shake, and Cheese Fries")
                        print("Your total is: $6")
                    elif fries_choice == "F":
                        print("\n~~~Order Summary~~~")
                        print("Strawberry Shake, and French Fries")
                        print("Your total is: $5")
                elif shake_choice == "N":
                    if fries_choice == "A":
                        print("\n~~~Order Summary~~~")
                        print("Neapolitan Shake, and Animal Fries")
                        print("Your total is: $9")
                    elif fries_choice == "C":
                        print("\n~~~Order Summary~~~")
                        print("Neapolitan Shake, and Cheese Fries")
                        print("Your total is: $8")
                    elif fries_choice == "F":
                        print("\n~~~Order Summary~~~")
                        print("Neapolitan Shake, and French Fries")
                        print("Your total is: $7")
        else:  # shake only
            if shake_choice == "V":
                print("\n~~~Order Summary~~~")
                print("Vanilla Shake")
                print("Your total is: $3")
            elif shake_choice == "C":
                print("\n~~~Order Summary~~~")
                print("Chocolate Shake")
                print("Your total is: $3")
            elif shake_choice == "S":
                print("\n~~~Order Summary~~~")
                print("Strawberry Shake")
                print("Your total is: $3")
            elif shake_choice == "N":
                print("\n~~~Order Summary~~~")
                print("Neapolitan Shake")
                print("Your total is: $5")
else:
    fries_yes_no = input("Would you like fries? Y/N\n")
    if fries_yes_no == "n" or fries_yes_no == "N":
        print("\n~~~Order Summary~~~")
        print("Not Hungry? That's OK... Have a nice day!")
    else:
        print("~~ Fries Menu ~~~")
        print("\tA : Animal Fries ($4)")
        print("\tC : Cheese Fries ($3)")
        print("\tF : French Fries ($2)")
        fries_choice = input("Please make a selection from the above:\n")
        if fries_choice != "A" and fries_choice != "C" and fries_choice != "F":
            print(f"{fries_choice}: Invalid selection")
            print("\n~~~Order Summary~~~")
            print("Not Hungry? That's OK... Have a nice day!")
        else:  # fries only
            if fries_choice == "A":
                print("\n~~~Order Summary~~~")
                print("Animal Fries")
                print("Your total is: $4")
            elif fries_choice == "C":
                print("\n~~~Order Summary~~~")
                print("Cheese Fries")
                print("Your total is: $3")
            elif fries_choice == "F":
                print("\n~~~Order Summary~~~")
                print("Animal Fries")
                print("Your total is: $4")
