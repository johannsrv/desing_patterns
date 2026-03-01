from pizza import Pizza

class PizzaBuilder:
    def set_dough(self, dough):
        pass
    
    def set_sauce(self, sauce):
        pass
    
    def set_topping(self, topping):
        pass
    

class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def set_dough(self):
        self.pizza._dough = "regular" # puedes usar un enum 
    
    def set_sauce(self):
        self.pizza._sauce = "tomato"
    
    def set_topping(self):
        self.pizza._topping = "mozzarella"
