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
}

def get_report():
    print(resources)
    print(money)
def check_ingredients(coffee):
    for x in coffee['ingredients']:
        if resources[x] - coffee['ingredients'][x] > 0:
            print('there is enough')
            return True
        else:
            print(f'there is not enough {x}')
            break
def make_payment(coffee):
    global money
    quarters = int(input('How many quarters?')) * 0.25
    dime = int(input('How many dimes?')) * 0.10
    nickel = int(input('How many nickels?')) * 0.05
    pennies = int(input('How many pennies?')) * 0.01
    total_payment =  quarters + dime + nickel + pennies
    cost = MENU[coffee]['cost']
    money = money + cost
    change = total_payment - cost
    print(f'Your change is ${change}.')

    if total_payment >= MENU[coffee]['cost']:
        return True
    else:
        print('insufficient funds')
        return False

def make_coffee(coffee, coffeename):
    for x in coffee['ingredients']:
        resources[x] = resources[x] - coffee['ingredients'][x]
    print(f'Here is your {coffeename}')


money = 0
machine_on = True
while machine_on:
    coffee = input('What would you like? (espresso/latte/cappuccino):\n')
    if coffee == 'off':
        machine_on = False
    elif coffee == 'report':
        get_report()
    elif coffee == 'latte':
        is_enough = check_ingredients(MENU['latte'])
        if is_enough:
            print('Now i need your money')
            if make_payment(coffee):
                print('now i will make the coffee')
                make_coffee(MENU[coffee], coffee)
        else:
            print('there were not enough ingredients')
    elif coffee == 'espresso':
        is_enough = check_ingredients(MENU['latte'])
        if is_enough:
            print('Now i need your money')
            if make_payment(coffee):
                print('now i will make the coffee')
                make_coffee(MENU[coffee], coffee)
        else:
            print('there were not enough ingredients')
    elif coffee == 'cappuccino':
        is_enough = check_ingredients(MENU['latte'])
        if is_enough:
            print('Now i need your money')
            if make_payment(coffee):
                print('now i will make the coffee')
                make_coffee(MENU[coffee], coffee)
        else:
            print('there were not enough ingredients')
