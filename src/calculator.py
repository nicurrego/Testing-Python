def sum(a,b):
    """
    >>> sum(5,7)
    12
    """
    return a+b
def substract(a,b):
    """
    >>> substract(10, 0)
    10
    """
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    """
    >>> divide(10,0)
    Traceback (most recent call last):
    ValueError: Can not divide by 0
    """
    if b == 0:
        raise ValueError('Can not divide by 0')
    return a/b