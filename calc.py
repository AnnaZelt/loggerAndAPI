from enum import Enum
import logging

logging.basicConfig(level=logging.INFO, filename='calc_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Actions(Enum):
    MULTIPLICATION = 1
    DIVISION = 2
    ADDITION = 3
    EXIT = 4

def menu():
    while True:
        for action in Actions:
            print(f"{action.value} - {action.name}")
        user_selection = Actions(int(input("What would you like to do? ")))
        
        if user_selection == Actions.MULTIPLICATION:
            mult()
        elif user_selection == Actions.DIVISION:
            div()
        elif user_selection == Actions.ADDITION:
            add()
        elif user_selection == Actions.EXIT:
            break

def mult():
    print("Choose two numbers: ")
    n1 = float(input("1st number: "))
    n2 = float(input("2nd number: "))
    try:
        result = n1 * n2
        logging.info("Multiplication result: %f", result)
        print(f"{n1} * {n2} = {result}")
    except Exception as e:
        logging.error("Error during multiplication: %s", str(e))

def div():
    print("Choose two numbers: ")
    n1 = float(input("1st number: "))
    n2 = float(input("2nd number: "))
    try:
        if n2 != 0:
            result = n1 / n2
            logging.info("Division result: %f", result)
            print(f"{n1} / {n2} = {result}")
        else:
            print("Cannot divide by zero.")
            logging.error("Cannot divide by zero.")
    except Exception as e:
        logging.error("Error during division: %s", str(e))

def add():
    print("Choose two numbers: ")
    n1 = float(input("1st number: "))
    n2 = float(input("2nd number: "))
    try:
        result = n1 + n2
        logging.info("Addition result: %f", result)
        print(f"{n1} + {n2} = {result}")
    except Exception as e:
        logging.error("Error during addition: %s", str(e))

if __name__ == "__main__":
    menu()
