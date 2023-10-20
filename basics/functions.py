# Functions
# functions provide a way to write a code one and use it later, thus removing redundancy
# in python we can use "def" keyword to defined a function or use the "lambda" for inline


# basic function
def hello_world():
    print("Hello, World!")


# function with a parameter
def greet(name):
    print(f"Hello {name}")


# function anotated with types
def sum(a: int, b: int) -> int:
    return a + b


# function with documentation & type anotation
def add_two(value: int) -> int:
    """
    A function that adds two to certain value

    Parameters:
        value {int}: the value to which we add 2
    Returns:
        {int}: result of the addition
    """

    assert isinstance(value, int), f"Invalid type of parameter 'value'"

    return value + 2


# function with *args
def sum(*args: int) -> int:
    result = 0

    for value in args:
        result += value

    return result


# keep adding number as much as you like...
print(sum(1, 2, 3, 4, 5, 6))


# function with **kwargs
def print_schema(**cfg) -> str:
    for key, value in cfg.items():
        print(f"{key}: {value}")


print_schema(
    cpu="Ryzen 5 5600x",
    ram="16GB DDR4 @2.6GHz",
    gpu="AMD RX 580 8GB",
    chipset="AMD B450",
    # ...keep adding (see kwargs.py for more info)
)
