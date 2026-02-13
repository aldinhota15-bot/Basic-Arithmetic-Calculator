# dicts to define each calculation
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def div(a, b):
    return a / b

def mul(a, b):
    return a * b


# Main list that stores the menu and operation values
# History left blank for now
# Pins are stored also

calculator_menu = {
    1: {"Operation": "Addition", "Func": add, "Result": None, "History": "X", "PIN": "4345"},
    2: {"Operation": "Subtraction", "Func": sub, "Result": None, "History": "X", "PIN": "1023"},
    3: {"Operation": "Multiplication", "Func": mul, "Result": None, "History": "X", "PIN": "2031"},
    4: {"Operation": "Division", "Func": div, "Result": None, "History": "X", "PIN": "9865"}
}

# A dict to carry all functions and statements that interact with the menu list
# Has multiple retries attempt for failed PIN attempts
# Returns to menu if all retries used up
# If user inputs right PIN, it asks to enter their numbers or "Operands"
# uses a "Try/except" statement to prevent invalid inputs
# Stores the result for result chaining, but first asks if the user would like to return to the menu
# user can also reset the calculation back to its basic parameters

def menu(calculator_menu_id):
    menu = calculator_menu[calculator_menu_id]

    retries = 5
    while retries > 0:
        pin = input(f"Enter PIN to start {menu['Operation']}:")
        if pin == menu["PIN"]:
            print("Enter Operands:")
            while True:
                try:
                    a = float(input("Operand 1:"))
                    b = float(input("Operand 2:"))
                    break
                except ValueError:
                    print("Invalid Input, try again")
                
            result = menu["Func"](a, b)
            menu["Result"] = result
            print(f"Result: {result}")

            while True:
                print("\nOPTIONS:")
                print("1. Continue with Result")
                print("2. Reset")
                print("3. Exit")
                option = input("Choose: ")
                if option == "1":
                    a = menu["Result"]
                    while True:
                        try:
                            b = float(input("Operand: "))
                            break
                        except ValueError:
                            print("Invalid Input, try again.")
                    try:
                        result = menu["Func"](a, b)
                        menu["Result"] = result
                        print(f"Result: {result}")
                    except ZeroDivisionError:
                        print("SYNTAX ERROR")
                elif option == "2":
                    while True:
                        try:
                            a = float(input("Operand 1:"))
                            b = float(input("Operand 2:"))
                            break
                        except ValueError:
                            print("Invalid Input, Try again.")
                
                    result = menu["Func"](a, b)
                    menu["Result"] = result
                    print(f"Result: {result}")
                    continue
                elif option == "3":
                    return
                    
                else:
                    print("Invalid input")
                    
        else:
            retries -= 1
            print(f"Incorrect PIN, you have {retries} left.")
        if retries == 0:
            print("Returning to menu")
            return

# Menu functions that allow the dict to work
# Starts a loop of the menu
# also has a "Try/Except" statements to shield the program from bad input
# Also allows the user to exit the program entirely


loop = True
while loop:
    print("===CALCULATOR===")
    for calculator_menu_id, data in calculator_menu.items():
        print(f"{calculator_menu_id}. {data['Operation']}")
    try:
        choice = int(input("Choose an option.(1-5):"))
    except ValueError:
        print("Invalid option")
        continue

    if choice == 5:
        print("Goodbye")
        loop = False
    elif choice in calculator_menu:
        menu(choice)
    else:
        print("Invalid option")
