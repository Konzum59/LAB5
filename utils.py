"""Super cool code :3"""

from multiprocessing.managers import Value


def add(a: int, b: int) -> int:
    """This code is for adding"""
    return a + b


def subtract(a: int, b: int) -> int:
    """This code is for substracting"""
    return a - b


def multiply(a: int, b: int) -> int:
    """This code is for multiplying"""
    return a * b


def divide(a: int, b: int) -> float:
    """This code is for dividing"""
    return a / b


def convert_to_binary(a: int) -> str:
    if not isinstance(a, int):
        raise ValueError("Not an int")
    if a < 0 or a > 100:
        raise ValueError("Not in range")
    return bin(a)[2:]
