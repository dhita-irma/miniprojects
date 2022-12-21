# Armstrong numbers are equal to the sum of the powers of their digits
# Exponent is the length of the number, base 10

def is_armstrong_number(number: int) -> bool:
    """Is number the equal to sum of powers of digits?"""
    s = str(number)
    exp = len(s)
    return number == sum(int(digit) ** exp for digit in s)
