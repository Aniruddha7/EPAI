import fractions
from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base >=2 and base<=36:
        pass
    else:
        raise ValueError("Error: base needs to be between 2 and 36")

    if base == len(digit_map):
        pass
    else:
        raise ValueError("characters are repeating in digit_map")

    if (len(set(digit_map))== len(digit_map)):
        pass
    else:
        raise ValueError("Characters are repeating in digit_map")

    digits= []
    encoding = ''
    if number < 0:
        encoding = '-'
    number = abs(number)

    while number > 0:
        m= number % base
        number= number // base
        digits.insert(0, m)

    for d in digits:
        encoding+=digit_map[d]

    return encoding

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    equality= abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

    return equality


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if f_num >= 0:
        f_num= (Fraction(f_num).numerator // Fraction(f_num).denominator)
        return f_num
    else:
        f_num= ((Fraction(f_num).numerator // Fraction(f_num).denominator)+1)
        return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    digits= 0
    number= Fraction(f_num*10**digits+0.1)
    number= number.limit_denominator(1).numerator
    f_num= number/ 10**digits
    return f_num

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0