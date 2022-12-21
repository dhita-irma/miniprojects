# Armstrong numbers are equal to the sum of the powers of their digits
# Exponent is the length of the number, base 10

def is_armstrong_number(number):
    """Is number the equal to sum of powers of digits?"""
    number_str = str(number)
    digits = len(number_str)
    sum = 0
    for n in range(digits): 
        sum += int(number_str[n]) ** digits
    return sum == number
