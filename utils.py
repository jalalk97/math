from fractions import Fraction
from decimal import Decimal

DENOMINATOR_LIMIT = 100

def to_fraction(value):
    """
    Converts virous types of arguments to fractions
    Usage:
    >> to_fractions(0) returns Fraction(0, 1)
    >> to_fractions(5) returns Fraction(5, 1)
    >> to_fractions([3, 5, 9]) returns [Fraction(3, 1), Fraction(5, 1), Fraction(9, 1)]
    >> to_fractions([3.9, 9/8, 4]) returns [Fraction(39, 10), Fraction(9, 8), Fraction(4, 1)] 
    """
    if isinstance(value, Fraction):
        value = value.limit_denominator(DENOMINATOR_LIMIT)
    elif isinstance(value, (int, float, Decimal, str)):
        value = Fraction(value).limit_denominator(DENOMINATOR_LIMIT)
    elif isinstance(value, list):
        value =  [Fraction(x).limit_denominator(DENOMINATOR_LIMIT) for x in value]
    else:
        raise TypeError('Invalid type', value, type(value))

    return value
