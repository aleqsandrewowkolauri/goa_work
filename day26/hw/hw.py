# homework 2 
def sum_of_two_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# homework 3
def is_even_or_odd(n):
    """Determines whether a given integer is even or odd."""
    return "Even" if n % 2 == 0 else "Odd"

# homework 4
def reverse_string(s):
    """Returns the reversed version of the given string using slicing."""
    return s[::-1]

# homework 5
def find_maximum(numbers):
    """Returns the maximum value from a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    return max(numbers)

# homework 6 
def factorial(n):
    """Calculates the factorial of a given number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)