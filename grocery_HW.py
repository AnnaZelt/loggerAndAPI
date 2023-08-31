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
        return (f"{self.product_name}: {self.product_price} NIS\n{self.amount_in_storage} units in stock.\n")

class Cart(Product):
    def __init__(self) -> None:
        self.product_list = []
        self.total = 0

    def __str__(self):
        return "\n".join(f"{product.product_name} x{product.amount_in_storage}" for product in self.product_list)+f"\n\nTotal: {self.total} NIS"
    
    def add_product(self, product):
        self.product_list.append(product)

def menu():
    global cart
    while(True):
        for action in Actions:
            print(f"{action.value} - {action.name}")
        user_selection=Actions(int(input("What would you like to do? ")))
        if user_selection == Actions.ADD_TO_CART: 
            add_to_cart()
        # if user_selection == Actions.ADD_TO_CART: 
        #     selected_name = input("Add: (by name) ")
        #     for product in products:
        #         if str(selected_name.lower()) == str(product.product_name):
        #             # cart_product = Product("PH",0,0)
        #             if cart.product_list == []:
        #                 cart_product = product
        #                 cart_product.amount_in_storage += 1
        #                 cart.add_product(cart_product)
        #                 cart.total += cart_product.product_price
        #             for cart_product in cart.product_list:
        #                 # cart_product = Product("PH",0,0)    
        #                 if cart_product.amount_in_storage == 0:
        #                     cart_product.amount_in_storage += 1
        #                     cart.add_product(cart_product)
        #                     cart.total += cart_product.product_price
        #                 if cart_product.amount_in_storage > 0:
        #                     cart_product = product   
        #                     cart_product.amount_in_storage += 1
        #                     cart.total += cart_product.product_price
        #         # else: print("Unfamiliar product.")            
        #     print("\n")
        if user_selection == Actions.DISPLAY_PRODUCTS:
            display_products()
        if user_selection == Actions.DISPLAY_CART:
            display_cart()
        if user_selection == Actions.EXIT: 
            save()
            return

def display_cart():
    print("\nProducts in cart:")
    print(f"{cart}\n")

def display_products():
    print("\nAvailable products: ")
    for product in products:
        print(product)

def add_to_cart():
    selected_name = input("Add: (by name) ").lower()
    product_found = False            
    for cart_product in cart.product_list:
        if cart_product.product_name.lower() == selected_name:
            cart_product.amount_in_storage += 1
            cart.total += cart_product.product_price
            product_found = True
            print(f"Added 1 {cart_product.product_name} to cart.")
            break 
    if not product_found:
        matching_products = [product for product in products if product.product_name.lower() == selected_name]
        if matching_products:
            new_cart_product = Product(matching_products[0].product_name, matching_products[0].product_price, 1)
            cart.add_product(new_cart_product)
            cart.total += new_cart_product.product_price
            print(f"Added 1 {new_cart_product.product_name} to cart.")
        else:
            print("Product not found.")
    print("\n")

def save():
    pass

def load():
    pass

cart = Cart()
DEBUG = 1
def testing():
    global products
    if DEBUG:
        banana = Product("banana", 10, 10)
        apple = Product("apple", 9, 4)
        wipes = Product("wipes", 31, 2)
        cheese = Product("cheese", 32, 7)
        apple_juice = Product("apple juice", 21, 4)
        toy = Product("toy", 45, 8)
        milk = Product("milk", 11, 13)
        products = [banana,apple,wipes,cheese,apple_juice,toy,milk]
    else: pass    
        
if __name__ == "__main__":
    testing()
    load()
    menu()
    