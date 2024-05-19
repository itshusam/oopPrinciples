This module defines classes representing different types of products.

Classes:
- Product: A base class representing a generic product.
- Book: A subclass of Product representing a book product.
- Electronic: A subclass of Product representing an electronic product.
- Clothing: A subclass of Product representing a clothing product.

Each class has attributes and methods to store and display product information.

Attributes:
- Product:
    - product_id (str): The unique identifier of the product.
    - name (str): The name of the product.
    - price (float): The price of the product.

- Book (additional):
    - author (str): The author of the book.

- Electronic (additional):
    - specs (str): The specifications of the electronic product.

- Clothing (additional):
    - size (str): The size of the clothing product.

Methods:
- Product:
    - __init__(self, product_id, name, price): Initializes a Product object with the given ID, name, and price.
    - display_info(self): Displays the information of the product, including ID, name, and price.

- Book:
    - __init__(self, product_id, name, price, author): Initializes a Book object with the given ID, name, price, and author.
    - display_info(self): Displays the information of the book, including ID, name, price, and author.

- Electronic:
    - __init__(self, product_id, name, price, specs): Initializes an Electronic object with the given ID, name, price, and specifications.
    - display_info(self): Displays the information of the electronic product, including ID, name, price, and specifications.

- Clothing:
    - __init__(self, product_id, name, price, size): Initializes a Clothing object with the given ID, name, price, and size.
    - display_info(self): Displays the information of the clothing product, including ID, name, price, and size.
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

        
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specifications: {self.specs}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
