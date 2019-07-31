# Product Inventory Project
# Create an application which manages an inventory of products.
# Create a product class which has a price, id, and quantity on hand.
# Then create an inventory class which keeps track of various products and can sum up the inventory value.


class Product:

    def __init__(self, name, idnum, price, quantity=0):
        self.name = name
        self.idnum = idnum
        self.price = price
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.productlist = []

    def add_product(self, price, idnum, quantity):
        """Add a new product to the list"""
        self.productlist.append(Product(price, idnum, quantity))
        return self.productlist

    def product_quantity(self, product_name):
        """Display product quantity by looking at
        the product name in the list of product. """
        for product in self.productlist:
            if product == product_name:
                print(product.quantity)
            else:
                print("Product is not found in the inventory.")

    def display_product(self):
        """Display all of the products with the ID number and the quantity"""
        for product in self.productlist:
            print(f"{product.idnum} - {product.price} - {product.quantity}")




inventory1 = Inventory()
inventory1.add_product(50000, "A001", 12)
inventory1.add_product(25000, "B001", 54)
inventory1.display_product()