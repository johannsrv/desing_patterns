from cook import Cook
from pizza_build import MargheritaPizzaBuilder

if __name__ == "__main__":
    cook = Cook()
    margherita_builder = MargheritaPizzaBuilder()
    pizza = cook.make_pizza(margherita_builder)
    print(pizza)
