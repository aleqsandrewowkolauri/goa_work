
def count_sheeps(sheep):
    return sheep.count(True)


def no_space(x):
    return x.replace(" ", "")

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

def greet(name):
    return f"Hello, {name} how are you doing today?"

def boolean_to_string(b):
    return str(b)

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

def century(year):
    return (year + 99) // 100


def digitize(n):
    return [int(d) for d in str(n)[::-1]]

def maps(arr):
    return [x * 2 for x in arr]

def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

