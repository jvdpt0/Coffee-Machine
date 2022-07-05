MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def check_coins(coins):
    value = 0
    value += (coins['quarters'] * 0.25)
    value += (coins['dimes'] * 0.1)
    value += (coins['nickles'] * 0.05)
    value += (coins['pennies'] * 0.01)
    if value > MENU[choice]['cost']:
        over = value - MENU[choice]['cost']
        over = round(over, 2)
        value = value - over
        print(value)
        print(MENU[choice]['cost'])
        print(f"Here is ${over} dollars in change.")
        resources['money'] += value
        return 0
    elif MENU[choice]['cost'] == value:
        resources['money'] += value
        return 0
    else:
        return 1


machine_on = True
while machine_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    coins = {
        'quarters': 0,
        'dimes': 0,
        'nickles': 0,
        'pennies': 0,
    }
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        print(resources)
    else:
        drink = MENU[choice]
        drink_ingredients = drink['ingredients']
        if check_resources(drink_ingredients):
            coins['quarters'] = int(input('Insert the amount of quarters: '))
            coins['dimes'] = int(input('Insert the amount of dimes: '))
            coins['nickles'] = int(input('Insert the amount of nickles: '))
            coins['pennies'] = int(input('Insert the amount of pennies: '))
            print(coins)
            change = check_coins(coins)
            if change == 0:
                for item in drink_ingredients:
                    resources[item] -= drink_ingredients[item]
            print(f"Here is your {choice}. Enjoy!")
