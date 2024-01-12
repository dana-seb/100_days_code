# Calculator
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


# d = divide(100,2)
# print(d)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
   
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        next = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calcuation ")

        if next == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()