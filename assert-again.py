"""
    This is the main module for intro-unittest
"""


def sum_positive_numbers(num1: int, num2: int) -> int:
    """
        This functions takes two positive integer numbers and return its sum.

    Args:
        num1 (int): a positive integer number
        num2 (int): another positive integer number

    Returns:
        int: Sum of num1 and num2
    """
    assert num1 >= 0 and num2 >= 0, "Sorry, we can't work with negative numbers."

    return num1 + num2


resultado = sum_positive_numbers(10, 20)
print(f"El resultado de la suma es {resultado}")

resultado2 = sum_positive_numbers(-10, 20)
