"""
A store can have multiple departments. A department can hold multiple products.
The store has a name. Departments have names. Products have names and prices.
Soccer Ball is a Product.

Nouns tend to be classes.
If a noun "has" something, that something tends to be an attribute.
If a noun "is" something, that tends to imply inheritance.
Verbs tend to be methods.

has-a is also called "composition".

"""


class Store:
    """Holds information about a Store"""

    def __init__(self, name, departments=None):
        """Construct a new Store"""

        self.name = name

        """
        if departments is None:
            self.departments = []
        else:
            self.departments = departments
        """
        self.departments = [] if departments is None else departments

class Department:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class SportsBall(Product):
    def __init__(self, name, price, diameter):
        super().__init__(name, price)
        self.diameter = diameter

class SoccerBall(SportsBall):
    def __init__(self):
        super().__init__("soccer ball", 34.99, 22)

class BasketBall(SportsBall):
    def __init__(self):
        super().__init__("basket ball", 34.99, 23)

sporting_goods = Department("Sporting Goods")

sporting_goods.add_product(SoccerBall())
sporting_goods.add_product(SoccerBall())
sporting_goods.add_product(SoccerBall())
sporting_goods.add_product(SoccerBall())
sporting_goods.add_product(BasketBall())
sporting_goods.add_product(BasketBall())
sporting_goods.add_product(BasketBall())
sporting_goods.add_product(BasketBall())
sporting_goods.add_product(BasketBall())
