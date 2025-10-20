class MoneyMachine:

    currency = "$"

    coin_values = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints current profit"""
        print(f"🪙Money: {self.currency}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from the inserted coins"""
        print("Please, insert coins")
        for coin in self.coin_values:
            self.money_received += int(input(f"How many {coin}?  ")) * self.coin_values[coin]
        return self.money_received

    def make_payment(self, drink_cost):
        """Returns True if payment is accepted; False if money insufficient"""
        self.process_coins()
        if self.money_received >= drink_cost:
            change = round(self.money_received - drink_cost, 2)
            print(f"Here is your change: {self.currency}{change}🪙")
            self.profit += drink_cost
            self.money_received = 0
            return True
        else:
            print(f"😕Sorry, that's not enough money! You've paid {self.money_received}, the drink costs {drink_cost}")
            print(f"You need to insert {drink_cost - self.money_received:.2f}🪙 more!")
            self.money_received = 0
            return False