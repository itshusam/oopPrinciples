
from product import Book
from product import Electronic
from product import Clothing

my_book = Book("123", "harry potter", 29.99, "idk")
my_book.display_info()

my_phone = Electronic("321", "Smartphone", 499.99, "8gb ram, 128GB storage")
my_phone.display_info()

my_shirt = Clothing("231", "T-shirt", 19.99, "M")
my_shirt.display_info()