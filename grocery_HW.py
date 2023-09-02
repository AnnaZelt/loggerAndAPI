from grocery_helper import *

logging.basicConfig(level=logging.INFO,filename='grocery_HW_info.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

def menu():
    global cart
    while(True):
        user_selection = menu_selection()
        if user_selection == Actions.ADD_TO_CART:
            add_to_cart(cart,products)
        # if user_selection == Actions.ADD_TO_CART: 
            selected_name = input("Add: (by name) ")
            for product in products:
                if str(selected_name.lower()) == str(product.product_name):
                    # cart_product = Product("PH",0,0)
                    if cart.product_list == []:
                        cart_product = product
                        cart_product.amount_in_storage += 1
                        cart.add_product(cart_product)
                        cart.total += cart_product.product_price
                    for cart_product in cart.product_list:
                        # cart_product = Product("PH",0,0)    
                        if cart_product.amount_in_storage == 0:
                            cart_product.amount_in_storage += 1
                            cart.add_product(cart_product)
                            cart.total += cart_product.product_price
                        if cart_product.amount_in_storage > 0:
                            cart_product = product   
                            cart_product.amount_in_storage += 1
                            cart.total += cart_product.product_price
                # else: print("Unfamiliar product.")            
            print("\n")
        if user_selection == Actions.DISPLAY_PRODUCTS:
            display_products(products)
        if user_selection == Actions.DISPLAY_CART:
            display_cart(cart)
        if user_selection == Actions.EXIT: 
            save()
            logging.shutdown()
            return

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
    