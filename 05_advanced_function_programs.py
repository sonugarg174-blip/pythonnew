# ADVANCED PYTHON FUNCTION PROGRAMS – LESSON 25
from functools import reduce

def default_arguments(name, message="Welcome"):
    return f"{message}, {name}!"

def variable_arguments(*numbers):
    return sum(numbers)

def keyword_arguments(**details):
    for key, value in details.items():
        print(key, ":", value)

def lambda_function():
    square = lambda number: number ** 2
    print("Lambda square:", square(6))

def map_function():
    numbers = [1, 2, 3, 4]
    print("Map result:", list(map(lambda n: n * 2, numbers)))

def filter_function():
    numbers = [1, 2, 3, 4, 5, 6]
    print("Even numbers:", list(filter(lambda n: n % 2 == 0, numbers)))

def reduce_function():
    numbers = [1, 2, 3, 4, 5]
    print("Product:", reduce(lambda x, y: x * y, numbers))

def recursive_factorial(n):
    if n < 0:
        raise ValueError("Enter a non-negative number")
    if n in (0, 1):
        return 1
    return n * recursive_factorial(n - 1)

def generator_function(limit):
    for number in range(1, limit + 1):
        yield number

def demonstrate_functions():
    print("1. Default argument:", default_arguments("Riya"))
    print("2. *args total:", variable_arguments(10, 20, 30))
    print("3. **kwargs:")
    keyword_arguments(name="Aman", course="BCA", semester=3)
    print("4.")
    lambda_function()
    print("5.")
    map_function()
    print("6.")
    filter_function()
    print("7.")
    reduce_function()
    print("8. Factorial:", recursive_factorial(5))
    print("9. Generator:", list(generator_function(5)))

if __name__ == "__main__":
    demonstrate_functions()
