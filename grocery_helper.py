
from enum import Enum
import logging

logging.basicConfig(level=logging.INFO,filename='grocery_HW_info.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

class Actions(Enum):
    DISPLAY_PRODUCTS = 1
    ADD_TO_CART = 2
    DISPLAY_CART = 3
    EXIT = 4

class Product:
    def __init__(self,product_name,product_price,amount_in_storage) -> None:
        self.product_name = product_name
        self.product_price = product_price
        self.amount_in_storage = amount_in_storage

    def __str__(self) -> str:
        return (f"{self.product_name}: {self.product_price} NIS\n{self.amount_in_storage} units in stock.\n")
    
    def add_stock(self):
        self.amount_in_storage = int((input("Add to stock: ")))
        logging.info("Stock changed.", exc_info=True)
        
class Cart(Product):
    def __init__(self) -> None:
        #Initializes an empty list designed for Product class objects
        self.product_list = []
        self.total = 0

    def __str__(self):
        return "\n".join(f"{product.product_name} x{product.amount_in_storage}" for product in self.product_list)+f"\n\nTotal: {self.total} NIS"
    
    def add_product(self, product):
        self.product_list.append(product)
        logging.info("Product added.", exc_info=True)

#Returns a selected action
def menu_selection():
    for action in Actions:
        print(f"{action.value} - {action.name}")
    user_selection=Actions(int(input("What would you like to do? ")))
    logging.info("Menu selection.", exc_info=True) 
    return user_selection

def display_cart(cart):
    print("\nProducts in cart:")
    print(f"{cart}\n")
    logging.info("Cart display.", exc_info=True)

def display_products(products):
    print("\nAvailable products: ")
    for product in products:
        print(product)
    logging.info("Products display.", exc_info=True)            

def add_to_cart(cart,products):
    #Searches in the producs object by name
    selected_name = input("Add: (by name) ").lower()
    product_found = False   
    #Iterates through the cart and adds 1 amount and x1 price to the cart total, of the selected product, 
    # if a match is found in the cart       
    for cart_product in cart.product_list:
        if cart_product.product_name.lower() == selected_name:
            cart_product.amount_in_storage += 1
            cart.total += cart_product.product_price
            product_found = True
            print(f"Added 1 {cart_product.product_name} to cart.")
            break
    #Else creates a temporary new_cart_product object and adds a copy of the selected product from the matching_products object
    # (which copies the matching product from the product object) to the cart with x1 amount and adds to the cart total    
    if not product_found:
        matching_products = [product for product in products if product.product_name.lower() == selected_name]
        if matching_products:
            new_cart_product = Product(matching_products[0].product_name, matching_products[0].product_price, 1)
            cart.add_product(new_cart_product)
            cart.total += new_cart_product.product_price
            print(f"Added 1 {new_cart_product.product_name} to cart.")
        logging.info("Added new item to cart.", exc_info=True)
    print("\n")

def save():
    pass

def load():
    pass
