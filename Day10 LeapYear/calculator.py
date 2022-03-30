from artt import logo


# ADD
def add(n1, n2):
    """Adds two number and returns the result"""
    return n1 + n2


# subtract
def subtract(n1, n2):
    """Subtracts two number and returns the result"""
    return n1 - n2


# multiply
def multiply(n1, n2):
    """Multipllies two number and returns the result"""
    return n1 * n2


# divide
def divide(n1, n2):
    """Divides two number and returns the result"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


print(logo)


def calculator():
    num1 = float(input("What's the first number?: "))
    for x in operations:
        print(x)

    calculate = True

    while calculate:
        operator = input("Pick an operation?: ")
        num2 = float(input("What's the Next number?: "))

        result = operations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {result} ")
        continue_calculation = input(f"Type 'y to contain calculating with {result}, or type 'n' to start over.: ")

        if continue_calculation == 'y':
            num1 = result
        else:
            continue_calculation = False
            calculator()


calculator()
