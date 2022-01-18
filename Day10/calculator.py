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

num1 = int(input("What's the first number?: "))
for x in operations:
    print(x)
operator = input("Pick an operation?: ")
num2 = int(input("What's the second number?: "))

result = operations[operator](num1, num2)

print(f"{num1} {operator} {num2} = {result} ")

