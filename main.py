# The Coffee Machine
from stuff import *
from tqdm import tqdm
import time

print("Good Morning\nType 'options' to see the available options")


def progress_bar():
    for _ in tqdm(range(100), ncols=50, ascii="_#"):
        time.sleep(0.03)
    pass


def print_options():
    for key, value in Options.items():
        print(key, value)


def calculate_coins():
    global price
    price = 0
    for key, value in Coins.items():
        cost = input(f"How many {key}: ")
        while not cost.isdigit():
            print(f"Invalid Value '{cost}'")
            cost = input(f"How many {key}: ")
        cost = int(cost)
        price += cost * value
        price = round(price, 2)
    print(f"You've inserted ${price}")
    return price


def make_espresso():
    print(f"Cost $1.5")
    if resources['water'] < 50 or resources['coffee'] < 18:
        if resources['water'] < 50:
            print("Sorry! Not enough water.")
        elif resources['coffee'] < 18:
            print("Sorry! Not enough coffee.")
        return 0
    elif calculate_coins() < 1.5:
        if price == 0:
            print("You did not insert any coins!")
            return 0
        print(f"Sorry! Not enough money.\n Money refunded")
        return 0
    else:
        progress_bar()
        if price > 1.5:
            change = price - 1.5
            change = round(change, 2)
            print(f"Here's your change ${change} back")
        print("Here is your espresso ☕️, enjoy!")
        resources['water'] -= 50
        resources['coffee'] -= 18
        PROFIT['Money'] += 1.5


def make_latte():
    print(f"Cost $2.5")
    if resources['water'] < 200 or resources['coffee'] < 24 or resources['milk'] < 150:
        if resources['water'] < 200:
            print("Sorry! Not enough water.")
        elif resources['coffee'] < 24:
            print("Sorry! Not enough coffee.")
        elif resources['milk'] < 150:
            print("Sorry! Not enough milk.")
        return 0
    elif calculate_coins() < 2.5:
        if price == 0:
            print("You did not insert any coins!")
            return 0
        print("Sorry! Not enough money.\nMoney refunded..")
        return 0
    else:
        progress_bar()
        if price > 2.5:
            change = price - 2.5
            change = round(change, 2)
            print(f"Here's your change ${change} back")
        print("Here is your latte ☕️, enjoy!")
        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 24
        PROFIT['Money'] += 2.5


def make_cappuccino():
    print(f"Cost $3.0")
    if resources['water'] < 250 or resources['coffee'] < 24 or resources['milk'] < 100:
        if resources['water'] < 250:
            print("Sorry! Not enough water.")
        elif resources['coffee'] < 24:
            print("Sorry! Not enough coffee.")
        elif resources['milk'] < 100:
            print("Sorry! Not enough milk.")
        return 0
    elif calculate_coins() < 3.0:
        if price == 0:
            print("You did not insert any coins!")
            return 0
        print("Sorry! Not enough money.\nMoney refunded..")
        return 0
    else:
        progress_bar()
        if price > 3.0:
            change = price - 3.0
            change = round(change, 2)
            print(f"Here's your change ${change} back")
        print("Here is your cappuccino ☕️, enjoy!")
        resources['water'] -= 50
        resources['milk'] -= 100
        resources['coffee'] -= 18
        PROFIT['Money'] += 3.0


def print_report():
    progress_bar()
    print(
        "The current available resources:\n"
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}\n"
        f"Money: ${PROFIT['Money']}"
    )


turn_off = False
while not turn_off:
    option = input("Type something! ").lower()
    while not option in ['options', 'report', 'espresso', 'latte', 'cappuccino', 'off', ' ']:
        print_options()
        option = input("Type something! ").lower()
    if option == "options":
        print_options()
    elif option == "report":
        print_report()
    elif option == "espresso":
        make_espresso()
    elif option == "latte":
        make_latte()
    elif option == "cappuccino":
        make_cappuccino()
    elif option == "off":
        print("Have a good day! ☺️")
        turn_off = True
