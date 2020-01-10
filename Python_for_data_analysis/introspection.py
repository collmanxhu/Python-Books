b = [1, 2, 3]

print(dir(b))

def add_number(a, b):
    """
    Add two numbers together

    Returns
    --------
    the_sum:type of arguments
    """
    return a + b

print(add_number.__doc__)
print(type(add_number))
print(dir(add_number))