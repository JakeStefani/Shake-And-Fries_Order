shake_types = {
    "Vanilla": {
        "key": "V",
        "flavor": "Vanilla",
        "price": 3
    },
    "Chocolate": {
        "key": "C",
        "flavor": "Chocolate",
        "price": 3
    },
    "Strawberry": {
        "key": "S",
        "flavor": "Strawberry",
        "price": 3
    },
    "Neapolitan": {
        "key": "N",
        "flavor": "Neapolitan",
        "price": 5
    }
}

fry_types = {
      "Animal": {
        "key": "A",
        "type": "Animal Fries",
        "price": 4
      },
      "Cheese": {
        "key": "C",
        "type": "Cheese Fries",
        "price": 3
      },
      "French": {
        "key": "F",
        "type": "French Fries",
        "price": 2
      }
}

order = {}

menu_format = '{key} :' + (' ' * 5) + '{menu_item:<13}' + '  ' + '(${price})\n'

shake_menu = '~~~ Shake Menu ~~~\n' +\
        menu_format.format(key = 'V', menu_item = shake_types['Vanilla']['flavor'], price = shake_types['Vanilla']['price']) +\
        menu_format.format(key = 'C', menu_item = shake_types['Chocolate']['flavor'], price = shake_types['Chocolate']['price']) +\
        menu_format.format(key = 'S', menu_item = shake_types['Strawberry']['flavor'], price = shake_types['Strawberry']['price']) +\
        menu_format.format(key = 'N', menu_item = shake_types['Neapolitan']['flavor'], price = shake_types['Neapolitan']['price']) 

fry_menu = '~~~ Fries Menu ~~~\n' +\
        menu_format.format(key = 'A', menu_item = fry_types['Animal']['type'], price = fry_types['Animal']['price']) +\
        menu_format.format(key = 'C', menu_item = fry_types['Cheese']['type'], price = fry_types['Cheese']['price']) +\
        menu_format.format(key = 'F', menu_item = fry_types['French']['type'], price = fry_types['French']['price'])

print("~~~Welcome to Shakes & Fries~~~")
print("We'd love to take your order\n\n")

shake_yes_no = input("Would you like a shake? Y/N\n")

while shake_yes_no == 'y' or shake_yes_no == 'Y':
    print(shake_menu)
    shake_choice = input("Please make a selection: ")
    print("\n")
    if shake_choice == 'V' or shake_choice == 'C' or shake_choice == 'S' or shake_choice == 'N' or shake_choice == 'v' or shake_choice == 'c' or shake_choice == 's' or shake_choice == 'n':
        shake_amount = int(input("How many would you like to order?\n"))
        break
    else:
        print("~~~Invalid Selection~~~\n")

if shake_yes_no == 'y' or shake_yes_no == 'Y':
    if shake_choice == 'V' or shake_choice == 'v':
        order['shake'] = shake_types['Vanilla']
    elif shake_choice == 'C' or shake_choice == 'c':
        order['shake'] = shake_types['Chocolate']
    elif shake_choice == 'S' or shake_choice == 's':
        order['shake'] = shake_types['Strawberry']
    elif shake_choice == 'N' or shake_choice == 'n':
        order['shake'] = shake_types['Neapolitan']

if shake_yes_no == 'n' or shake_yes_no == 'N':
    print("\n")

fries_yes_no = input("Would you like fries? Y/N\n")

if (fries_yes_no == 'n' or fries_yes_no == 'N') and (shake_yes_no == 'n' or shake_yes_no == 'N'):
    print("\nNot Hungry? That's OK... Have a nice day!")

while fries_yes_no == 'y' or fries_yes_no == 'Y':
    print(fry_menu)
    fry_choice = input("Please make a selection: ")
    print("\n")
    if fry_choice == 'A' or fry_choice == 'a' or fry_choice == 'C' or fry_choice == 'c' or fry_choice == 'F' or fry_choice == 'f':
        fry_amount = int(input("How many would you like to order?\n"))
        break
    else:
        print("~~~Invalid Selection~~~\n")

if fries_yes_no == 'y' or fries_yes_no == 'Y':
    if fry_choice == 'A' or fry_choice == 'a':
        order['fries'] = fry_types['Animal']
    elif fry_choice == 'C' or fry_choice == 'c':
        order['fries'] = fry_types['Cheese']
    elif fry_choice == 'F' or fry_choice == 'f':
        order['fries'] = fry_types['French']

item = 'Item'
amount = 'Amount'

if shake_yes_no == 'y' or shake_yes_no == 'Y':
    order_shake = f"{order['shake']['flavor']} Shake"
    shake_price = float(order['shake']['price'] * shake_amount)
    shake_price = f"${float(shake_price):.2f}"

if fries_yes_no == 'y' or fries_yes_no == 'Y':
    order_fries = f"{order['fries']['type']}"
    fries_price = float(order['fries']['price'] * fry_amount)
    fries_price = f"${float(fries_price):.2f}"

if (shake_yes_no == 'y' or shake_yes_no == 'Y') and (fries_yes_no == 'y' or fries_yes_no == 'Y'):
    total = float(order['fries']['price'] * fry_amount) + float(order['shake']['price'] * shake_amount)

if (shake_yes_no == 'y' or shake_yes_no == 'Y') and (fries_yes_no == 'n' or fries_yes_no == 'N'):
    total = float(order['shake']['price'] * shake_amount)

if (shake_yes_no == 'n' or shake_yes_no == 'N') and (fries_yes_no == 'y' or fries_yes_no == 'Y'):
    total = float(order['fries']['price'] * fry_amount)

if (shake_yes_no == 'y' or shake_yes_no == 'Y') and (fries_yes_no == 'y' or fries_yes_no == 'Y'):
    print("~~~Order Summary~~~")
    print(f"{item:<19}" + f"{amount}" + '    ' + 'Price')
    print(f"{order_shake:<19}" + f"{shake_amount:<5}" + '     ' + f"{shake_price:>5}")
    print(f"{order_fries:<19}" + f"{fry_amount:<5}" + '     ' + f"{fries_price:>5}")
    print("")
    print("Total" + (" " * 24) + "$" + f"{float(total):.2f}")

if (shake_yes_no == 'y' or shake_yes_no == 'Y') and (fries_yes_no == 'n' or fries_yes_no == 'N'):
    print("~~~Order Summary~~~")
    print(f"{item:<19}" + f"{amount}" + '    ' + 'Price')
    print(f"{order_shake:<19}" + f"{shake_amount:<5}" + '     ' + f"{shake_price:>5}")
    print("")
    print("Total" + (" " * 24) + "$" + f"{float(total):.2f}")

if (shake_yes_no == 'n' or shake_yes_no == 'N') and (fries_yes_no == 'y' or fries_yes_no == 'Y'):
    print("~~~Order Summary~~~")
    print(f"{item:<19}" + f"{amount}" + '    ' + 'Price')
    print(f"{order_fries:<19}" + f"{fry_amount:<5}" + '     ' + f"{fries_price:>5}")
    print("")
    print("Total" + (" " * 24) + "$" + f"{float(total):.2f}")
