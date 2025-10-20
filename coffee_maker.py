class CoffeeMaker:
    """Models the coffee machine"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of the remain resources"""
        print(f"💧Water: {self.resources['water']}ml\n"
              f"🥛Milk: {self.resources['milk']}ml\n"
              f"☕Coffee: {self.resources['coffee']}ml")

    def is_resource_sufficient(self, drink):
        """Returns True if order can be made; False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}🫤")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name}! Enjoy☕!")
