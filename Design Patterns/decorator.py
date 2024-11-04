# Component Interface
class Coffee:
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 2  # Add cost of milk

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._coffee.cost() + 1  # Add cost of sugar

# Client Code
if __name__ == "__main__":
    # Start with a simple coffee
    my_coffee = SimpleCoffee()
    print("Cost of Simple Coffee:", my_coffee.cost())  # Output: 5

    # Add milk to the coffee
    my_coffee_with_milk = MilkDecorator(my_coffee)
    print("Cost of Coffee with Milk:", my_coffee_with_milk.cost())  # Output: 7

    # Add sugar to the coffee with milk
    my_coffee_with_milk_and_sugar = SugarDecorator(my_coffee_with_milk)
    print("Cost of Coffee with Milk and Sugar:", my_coffee_with_milk_and_sugar.cost())  # Output: 8
