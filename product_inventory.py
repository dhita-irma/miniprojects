# Product Inventory Project
# Create an application which manages an inventory of products.
# Create a product class which has a price, id, and quantity on hand.
# Then create an inventory class which keeps track of various products and can sum up the inventory value.


class Product:

    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity


class Inventory:

    def __init__(self, product):
        self.product = product
        