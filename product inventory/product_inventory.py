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

    def add_product(self, name, idnum, price, quantity):
        """Add a new product to the list"""
        self.productlist.append(Product(name, idnum, price, quantity))
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
            print(f"{product.name} - {product.idnum} - {product.price} - {product.quantity}")

    def inventory_value(self):
        total_value = 0
        for product in self.productlist:
            total_value += (product.price * product.quantity)
        return print(f"Total inventory value is: {total_value}")


inventory = Inventory()
inventory.add_product("Notebook", "S001", 3000, 200)
inventory.add_product("Pencil", "S002", 2000, 55)
inventory.add_product("Pen", "S003", 2500, 60)
inventory.display_product()
inventory.inventory_value()