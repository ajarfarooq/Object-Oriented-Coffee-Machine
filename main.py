
class MenuItem:
    def __init__(self,name,cost,ingredients):
        self.name=name
        self.cost=cost
        self.ingredients=ingredients


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 1.5, {"water": 200, "milk": 150, "coffee": 24}),
            MenuItem("espresso", 1.0, {"water": 50, "coffee": 18}),
            MenuItem("cappuccino", 2.0, {"water": 250, "milk": 100, "coffee": 24})
        ]

    def get_items(self):
        items = ""
        for item in self.menu:
            items += item.name + "/"
        return items[:-1]

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


class CoffeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry not enough {item}.")
                return False
        return True

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕")


class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def make_payment(self, cost):
        payment = float(input("Enter money: $"))
        if payment >= cost:
            self.profit += cost
            change = payment - cost
            if change > 0:
                print(f"Here is ${round(change, 2)} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

menu = Menu()
coffee_maker = CoffeMaker()
money_machine = MoneyMachine()

choice = input(f"What would you like? ({menu.get_items()}): ")

drink = menu.find_drink(choice)

if drink:
    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
else:
    print("Sorry, drink not available.")












































