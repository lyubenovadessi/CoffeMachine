import coffee_machine_logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_machine_on = True

while is_machine_on:
    print(coffee_machine_logo.logo)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_machine_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        try:
            drink = menu.find_drink(choice)
            if drink and coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        except AttributeError:
            print("Invalid drink selected or missing data in menu item.")