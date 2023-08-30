from enum import Enum

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
        return (f"{self.product_name}: {self.product_price}, {self.amount_in_storage} in stock.")
    
    def change_amount(self):
        self.amount_in_storage = 0

    
class Cart(Product):
    def __init__(self) -> None:
        self.product_list = []

    def __str__(self):
        return "\n".join(str(product) for product in self.product_list)
    
    def add_product(self, product):
        self.product_list.append(product)

def menu():
    global products,cart
    while(True):
        for action in Actions:
            print(f"{action.value} - {action.name}")
        user_selection=Actions(int(input("What would you like to do? ")))
        if user_selection == Actions.ADD_TO_CART: 
            for product in products:
                cart.add_product(product)
            print("\nProducts in cart:")
            print(cart)
        if user_selection == Actions.DISPLAY_CART: pass
        if user_selection == Actions.DISPLAY_CART: pass
        if user_selection == Actions.EXIT: 
            save()
            return

def save():
    pass

def load():
    pass
banana = Product("banana", 10, 10)
apple = Product("apple", 9, 4)
wipes = Product("wipes", 31, 2)
cheese = Product("cheese", 32, 7)
apple_juice = Product("apple juice", 21, 4)
toy = Product("toy", 45, 8)
milk = Product("milk", 11, 13)
products = [banana,apple,wipes,cheese,apple_juice,toy,milk]
cart = Cart()
DEBUG = 1
def testing():
    global cart, products
    if DEBUG:
        counter = 0
        for product in products:
            products[counter].amount_in_storage = 1
            cart.add_product(product)
            counter+=1
        print("\n[TEST]Products in cart:")
        print(cart)
           
if __name__ == "__main__":
    testing()
    load()