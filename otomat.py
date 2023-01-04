import time

coffee__types_and_prices = {"latte": 3.50,
                            "cappuccino": 3.75,
                            "espresso": 2.75,
                            "filter_coffee": 2.0,
                            "hot_chocolate": 2.5}

def order_coffee():
    print(" Welcome to our coffee automat! Please make your selection:")
    print("(1) Latte ($3.50)")
    print("(2) Cappuccino ($3.75)")
    print("(3) Espresso ($2.75)")
    print("(4) Filter Coffee ($2.0)")
    print("(5) Hot Chocolate ($2.50)")

    coffee_selection = int(input("Enter your selection: "))
    if coffee_selection == 1:
        coffee_type = "Latte"
    elif coffee_selection == 2:
        coffee_type = "Cappuccino"
    elif coffee_selection == 3:
        coffee_type = "Espresso"
    elif coffee_selection == 4:
        coffee_type = "Filter Coffe"
    elif coffee_selection == 5:
        coffee_type = "Hot Chocolate"
    else:
        print("Invalid coffee selection. Please try again.")
        order_coffee()

    sugar_level = int(input("Enter sugar level (0-3): "))
    if sugar_level == 0 or sugar_level == 1 or sugar_level == 2 or sugar_level == 3:
        print("Your choice of sugar has been confirmed.")
    else:
        print("Invalid coffee selection. Please try again.")
        order_coffee()

    milk_level = int(input("Please enter milk level (0-3) :"))
    if milk_level == 0 or milk_level == 1 or milk_level == 2 or milk_level == 3:
        print("Your choice of milk level has been confirmed.")
    else:
        print("Invalid coffee selection. Please try again.")
        order_coffee()
    coffee_order = {"type": coffee_type, "sugar": sugar_level, "milk": milk_level}
    order_confirmation = input("Press Enter to make the payment")
    print("Payment is in progress...")
    time.sleep(1.5)

    return coffee_order


def make_coffee(order):
    print("Making your coffee...")
    time.sleep(2)
    print("Here is your coffee:")
    print(f"{order['type']} with {order['sugar']} sugar(s) {order['milk']} milk_level ")

order = order_coffee()

make_coffee(order)

print("....ENJOY YOUR MEAL....")

