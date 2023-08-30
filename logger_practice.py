from enum import Enum
import logging

logging.basicConfig(level=logging.ERROR,filename='error.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO,filename='info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class Actions(Enum):
    MULTIPLICATION = 1
    DIVISION = 2
    ADDITION = 3
    EXIT = 4

def menu():
    global products,cart
    while(True):
        for action in Actions:
            print(f"{action.value} - {action.name}")
        user_selection=Actions(int(input("What would you like to do? ")))
        if user_selection == Actions.MULTIPLICATION:
            mult()  
        if user_selection == Actions.DIVISION: 
            div()
        if user_selection == Actions.ADDITION: 
            add()
        if user_selection == Actions.EXIT: return

def mult():
    print("Choose two numbers: ")
    n1=input("1st number: ")
    n2=input("2nd number: ")
    try:
        sum = n1*n2
    except Exception as e:
        logging.INFO(exc_info=True)
    return sum

def div(n1,n2):
    print("Choose two numbers: ")
    n1=input("1st number: ")
    n2=input("2nd number: ")
    try:
        sum = n1/n2
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    return sum

def add(n1,n2):
    print("Choose two numbers: ")
    n1=input("1st number: ")
    n2=input("2nd number: ")
    sum = n1+n2
    return sum