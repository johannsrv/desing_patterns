class Pizza:
    def __init__(self):
        self._dough = None
        self._sauce = None
        self._topping = None

    def __str__(self):
        return f"Pizza with {self._dough} dough, {self._sauce} sauce, and {self._topping} topping."