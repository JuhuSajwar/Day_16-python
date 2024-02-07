MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted in Indian Coffee Machine."""
    print("Please insert coins.")
    # Prompt the user for the number of each type of coin
    rupees_5 = int(input("How many 5 rupees coins?: "))
    rupees_10 = int(input("How many 10 rupees coins?: "))
    rupees_20 = int(input("How many 20 rupees coins?: "))
    rupees_50 = int(input("How many 50 rupees coins?: "))
    rupees_100 = int(input("How many 100 rupees notes?: "))
    rupees_200 = int(input("How many 200 rupees notes?: "))
    rupees_500 = int(input("How many 500 rupees notes?: "))
    rupees_2000 = int(input("How many 2000 rupees notes?: "))

    # Calculate the total value of all coins inserted in Indian rupees
    total_inr = (rupees_5 * 5) + (rupees_10 * 10) + (rupees_20 * 20) + (rupees_50 * 50) + \
                (rupees_100 * 100) + (rupees_200 * 200) + (rupees_500 * 500) + (rupees_2000 * 2000)
    
    return total_inr




def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








